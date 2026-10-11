"""Cogs, Claws & Capes - pack builder.

  python tools/build.py lock      resolve pack/pack.json against the Modrinth API -> pack/mods.lock.json
  python tools/build.py mrpack    write dist/<name>-<version>.mrpack (import into Prism / Modrinth App / ATLauncher)
  python tools/build.py server    build/refresh a dedicated server in server/ (Java 17 + Forge + server-side mods + overrides)
  python tools/build.py all       lock + mrpack + server

Only the Python standard library is used. The lock pins exact Modrinth version ids + hashes, so a build is
reproducible: re-run `lock` only when you WANT updates, then re-test the server boot before sharing.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "pack" / "pack.json"
LOCK = ROOT / "pack" / "mods.lock.json"
OVERRIDES = ROOT / "overrides"
SERVER_OVERRIDES = ROOT / "server-overrides"
DIST = ROOT / "dist"
SERVER = Path(os.environ["CCC_SERVER_DIR"]) if os.environ.get("CCC_SERVER_DIR") else ROOT / "server"  # override: a test copy
JDK = ROOT / "tools" / "jdk"
API = "https://api.modrinth.com/v2"
UA = {"User-Agent": "cogs-claws-capes-builder/0.1 (personal modpack)"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def download(url, dest, sha1=None):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and sha1 and hashlib.sha1(dest.read_bytes()).hexdigest() == sha1:
        return False
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=300) as r:
        data = r.read()
    if sha1 and hashlib.sha1(data).hexdigest() != sha1:
        raise SystemExit(f"ERROR sha1 mismatch for {url}")
    dest.write_bytes(data)
    return True


def side(value):
    return {"required": "required", "optional": "optional", "unsupported": "unsupported"}.get(value, "optional")


# ---------------------------------------------------------------- lock
def pick_version(project, mc, loader, pin):
    q = urllib.parse.urlencode({"loaders": json.dumps([loader]), "game_versions": json.dumps([mc])})
    versions = get(f"{API}/project/{project}/version?{q}")
    if pin:
        versions = [v for v in versions if v["version_number"] == pin or v["id"] == pin]
    if not versions:
        raise SystemExit(f"ERROR {project}: no {loader} {mc} version" + (f" matching pin {pin}" if pin else ""))
    releases = [v for v in versions if v["version_type"] == "release"]
    return (releases or versions)[0]  # API returns newest first


def cmd_lock():
    pack = json.loads(PACK.read_text(encoding="utf-8"))
    mc, loader, pins = pack["minecraft"], pack["loader"], pack.get("pins", {})
    wanted = [(slug, group) for group, slugs in pack["mods"].items() for slug in slugs]
    entries, seen = {}, {}
    queue = list(wanted)
    while queue:
        ref, group = queue.pop(0)
        proj = get(f"{API}/project/{ref}")
        if proj["id"] in seen:
            continue
        seen[proj["id"]] = proj["slug"]
        ver = pick_version(proj["id"], mc, loader, pins.get(proj["slug"]))
        f = next((x for x in ver["files"] if x["primary"]), ver["files"][0])
        entries[proj["slug"]] = {
            "title": proj["title"],
            "group": group,
            "project_id": proj["id"],
            "version_id": ver["id"],
            "version_number": ver["version_number"],
            "published": ver["date_published"][:10],
            "file": f["filename"],
            "url": f["url"],
            "sha1": f["hashes"]["sha1"],
            "sha512": f["hashes"]["sha512"],
            "size": f["size"],
            "client": side(proj["client_side"]),
            "server": side(proj["server_side"]),
        }
        for d in ver["dependencies"]:
            if d["dependency_type"] == "required" and d.get("project_id") and d["project_id"] not in seen:
                queue.append((d["project_id"], f"dependency of {proj['slug']}"))
    # A mod a player needs on both sides must never be marked server-unsupported by a sloppy project page,
    # except the known client-only ones listed here.
    client_only = {"embeddium", "entityculling", "immediatelyfast", "mouse-tweaks", "xaeros-minimap", "xaeros-world-map"}
    for slug, e in entries.items():
        if slug in client_only:
            e["server"] = "unsupported"
    lock = {"minecraft": mc, "loader": loader, "loader_version": pack["loader_version"],
            "mods": dict(sorted(entries.items()))}
    LOCK.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8")
    direct = {s for s, _ in wanted}
    deps = [s for s in entries if s not in direct]
    print(f"lock: {len(entries)} mods ({len(direct)} listed + {len(deps)} dependencies: {', '.join(sorted(deps))})")


def load_lock():
    if not LOCK.exists():
        raise SystemExit("ERROR pack/mods.lock.json missing - run: python tools/build.py lock")
    return json.loads(LOCK.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- mrpack
def cmd_mrpack():
    pack = json.loads(PACK.read_text(encoding="utf-8"))
    lock = load_lock()
    files = [{
        "path": f"mods/{e['file']}",
        "hashes": {"sha1": e["sha1"], "sha512": e["sha512"]},
        "env": {"client": "unsupported" if e["client"] == "unsupported" else "required", "server": e["server"]},
        "downloads": [e["url"]],
        "fileSize": e["size"],
    } for e in lock["mods"].values()]
    index = {
        "formatVersion": 1, "game": "minecraft",
        "versionId": pack["version"], "name": pack["name"], "summary": pack["summary"],
        "files": files,
        "dependencies": {"minecraft": lock["minecraft"], "forge": lock["loader_version"]},
    }
    DIST.mkdir(exist_ok=True)
    out = DIST / f"cogs-claws-capes-{pack['version']}.mrpack"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("modrinth.index.json", json.dumps(index, indent=2))
        n = 0
        for p in OVERRIDES.rglob("*"):
            if p.is_file():
                z.write(p, "overrides/" + p.relative_to(OVERRIDES).as_posix())
                n += 1
    print(f"mrpack: {out} ({len(files)} mods, {n} override files)")


# ---------------------------------------------------------------- server
def java_exe():
    exe = JDK / "bin" / ("java.exe" if os.name == "nt" else "java")
    if exe.exists():
        return exe
    print("server: downloading Eclipse Temurin 17 JRE (portable, into tools/jdk)")
    os_name = "windows" if os.name == "nt" else "linux"
    ext = "zip" if os.name == "nt" else "tar.gz"
    url = f"https://api.adoptium.net/v3/binary/latest/17/ga/{os_name}/x64/jre/hotspot/normal/eclipse"
    tmp = ROOT / "tools" / f"jre17.{ext}"
    download(url, tmp)
    staging = ROOT / "tools" / "jdk_extract"
    shutil.unpack_archive(str(tmp), str(staging))
    inner = next(staging.iterdir())
    inner.rename(JDK)
    staging.rmdir()
    tmp.unlink()
    return exe


# server.properties keys the pack owns: synced from server-overrides on every build (the rest stays as you set it).
MANAGED_PROPERTIES = ("online-mode", "enforce-secure-profile", "allow-flight", "white-list", "enforce-whitelist")


def server_running(server=None):
    """True while a server has this world open: Minecraft holds an exclusive lock on world/session.lock."""
    server = server or SERVER
    props = server / "server.properties"
    level = "world"
    if props.exists():
        for line in props.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("level-name="):
                level = line.split("=", 1)[1].strip() or "world"
    lock = server / level / "session.lock"
    if not lock.exists():
        return False
    try:
        with open(lock, "rb") as f:
            f.read(1)
        return False
    except PermissionError:
        return True


def sync_managed_properties():
    live, seed = SERVER / "server.properties", SERVER_OVERRIDES / "server.properties"
    if not (live.exists() and seed.exists()):
        return
    want = {}
    for line in seed.read_text(encoding="utf-8").splitlines():
        k, _, v = line.partition("=")
        if k.strip() in MANAGED_PROPERTIES:
            want[k.strip()] = v.strip()
    lines, changed = live.read_text(encoding="utf-8").splitlines(), []
    for i, line in enumerate(lines):
        k, _, v = line.partition("=")
        if k.strip() in want and v.strip() != want[k.strip()]:
            changed.append(f"{k.strip()}: {v.strip()} -> {want[k.strip()]}")
            lines[i] = f"{k.strip()}={want[k.strip()]}"
    if changed:
        live.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("server: server.properties updated: " + "; ".join(changed))


def cmd_server():
    if server_running():
        raise SystemExit("ERROR the server is running. Type `stop` in its window, wait for it to close, then run this again.")
    lock = load_lock()
    SERVER.mkdir(exist_ok=True)
    java = java_exe()
    fv = f"{lock['minecraft']}-{lock['loader_version']}"
    if not (SERVER / "libraries" / "net" / "minecraftforge" / "forge" / fv).exists():
        inst = SERVER / f"forge-{fv}-installer.jar"
        download(f"https://maven.minecraftforge.net/net/minecraftforge/forge/{fv}/forge-{fv}-installer.jar", inst)
        print(f"server: installing Forge {fv}")
        subprocess.run([str(java), "-jar", inst.name, "--installServer"], cwd=SERVER, check=True,
                       stdout=subprocess.DEVNULL)
        inst.unlink()
        (SERVER / f"forge-{fv}-installer.jar.log").unlink(missing_ok=True)
    mods = SERVER / "mods"
    mods.mkdir(exist_ok=True)
    keep = set()
    fetched = 0
    for e in lock["mods"].values():
        if e["server"] == "unsupported":
            continue
        keep.add(e["file"])
        fetched += download(e["url"], mods / e["file"], e["sha1"])
    # Remove only jars this tool put there earlier and no longer wants (listed in the previous manifest).
    manifest = SERVER / ".pack-mods.json"
    old = set(json.loads(manifest.read_text())) if manifest.exists() else set()
    for name in old - keep:
        (mods / name).unlink(missing_ok=True)
    manifest.write_text(json.dumps(sorted(keep)))
    # Pack overrides (kubejs, config, defaultconfigs) then server-only overrides (server.properties etc.).
    # server.properties / ops / whitelist are only seeded if missing so your live edits are never overwritten.
    for src in (OVERRIDES, SERVER_OVERRIDES):
        for p in src.rglob("*"):
            if not p.is_file():
                continue
            rel = p.relative_to(src)
            dest = SERVER / rel
            if src == SERVER_OVERRIDES and dest.exists():
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dest)
    sync_managed_properties()
    # Running the server means accepting the Minecraft EULA (https://aka.ms/MinecraftEULA) - see docs/HOSTING.md.
    (SERVER / "eula.txt").write_text("eula=true\n")
    jvm = SERVER / "user_jvm_args.txt"
    if not jvm.exists() or "Xmx" not in jvm.read_text():
        jvm.write_text("-Xms6G\n-Xmx8G\n")
    args = "win_args.txt" if os.name == "nt" else "unix_args.txt"
    (SERVER / "start.bat").write_text(
        "@echo off\r\ncd /d \"%~dp0\"\r\n"
        f"\"{java}\" @user_jvm_args.txt @libraries/net/minecraftforge/forge/{fv}/{args} nogui %*\r\n"
        "pause\r\n")
    (SERVER / "run.bat").unlink(missing_ok=True)
    (SERVER / "run.sh").unlink(missing_ok=True)
    print(f"server: {len(keep)} server-side mods ({fetched} downloaded) in {SERVER}")
    print("server: start with server\\start.bat")


if __name__ == "__main__":
    steps = {"lock": [cmd_lock], "mrpack": [cmd_mrpack], "server": [cmd_server],
             "all": [cmd_lock, cmd_mrpack, cmd_server]}
    if len(sys.argv) != 2 or sys.argv[1] not in steps:
        raise SystemExit(__doc__)
    for step in steps[sys.argv[1]]:
        step()

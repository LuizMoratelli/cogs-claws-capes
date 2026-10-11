"""Add / remove players on the server whitelist with the UUID the server will really see.

The server runs online-mode=false + TrueUUID. A PAID account that TrueUUID verifies joins with its real Mojang UUID; an
OFFLINE account joins with the offline UUID (md5 of "OfflinePlayer:<name>"). The vanilla whitelist matches by UUID, and in
offline mode `whitelist add NAME` always writes the offline UUID - so a paid friend added that way is refused.

  python tools/whitelist.py add NAME --paid       real Mojang UUID (fails if the name has no paid account)
  python tools/whitelist.py add NAME --offline    offline UUID (friends without a paid account)
  python tools/whitelist.py remove NAME
  python tools/whitelist.py list

Then type `whitelist reload` in the server window (no restart needed).
"""
import hashlib
import json
import sys
import urllib.request
import uuid
from pathlib import Path

WL = Path(__file__).resolve().parents[1] / "server" / "whitelist.json"


def offline_uuid(name):
    # Java: UUID.nameUUIDFromBytes(("OfflinePlayer:" + name).getBytes(UTF_8)) - an MD5 (version 3) UUID
    b = bytearray(hashlib.md5(("OfflinePlayer:" + name).encode("utf-8")).digest())
    b[6] = (b[6] & 0x0F) | 0x30
    b[8] = (b[8] & 0x3F) | 0x80
    return str(uuid.UUID(bytes=bytes(b)))


def paid_uuid(name):
    try:
        with urllib.request.urlopen(f"https://api.mojang.com/users/profiles/minecraft/{name}", timeout=20) as r:
            j = json.load(r)
    except urllib.error.HTTPError as e:
        if e.code in (204, 404):
            raise SystemExit(f"ERROR '{name}' has no paid Minecraft account. Use --offline for friends without one.")
        raise
    return str(uuid.UUID(j["id"])), j["name"]


def load():
    return json.loads(WL.read_text(encoding="utf-8")) if WL.exists() else []


def save(entries):
    WL.write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")


def main(argv):
    if not argv or argv[0] not in ("add", "remove", "list"):
        raise SystemExit(__doc__)
    if not WL.parent.exists():
        raise SystemExit(f"ERROR no server at {WL.parent} - run: python tools/build.py server")
    entries = load()
    if argv[0] == "list":
        for e in entries:
            kind = "offline" if e["uuid"] == offline_uuid(e["name"]) else "paid"
            print(f"{e['name']:20} {kind:8} {e['uuid']}")
        return
    if len(argv) < 2:
        raise SystemExit(__doc__)
    name = argv[1]
    entries = [e for e in entries if e["name"].lower() != name.lower()]
    if argv[0] == "add":
        if "--paid" in argv:
            uid, name = paid_uuid(name)
        elif "--offline" in argv:
            uid = offline_uuid(name)
        else:
            raise SystemExit("ERROR say --paid or --offline (does this friend own Minecraft?)")
        entries.append({"uuid": uid, "name": name})
        print(f"added {name} ({'paid' if '--paid' in argv else 'offline'}) {uid}")
    else:
        print(f"removed {name}")
    save(entries)
    print("now type in the server window:  whitelist reload")


if __name__ == "__main__":
    main(sys.argv[1:])

r"""Apply the pack's hero keybind layout to one Prism instance, or restore the previous keys. Game must be CLOSED.

  python tools/fix_keybinds.py [INSTANCE_DIR] [--hold-sprint]     apply extras/keybinds-hero.txt (backs up first)
  python tools/fix_keybinds.py [INSTANCE_DIR] --restore           put back the newest options.txt.bak-* backup

Default instance: the newest cogs-claws-capes* folder in %APPDATA%\PrismLauncher\instances.
The layout (extras/keybinds-hero.txt) is the same file the "-hero-keys" .mrpack ships as its options.txt.
--hold-sprint also installs extras/hold_to_sprint.js (sprint only while the key is held).
"""
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAYOUT_FILE = ROOT / "extras" / "keybinds-hero.txt"


def load_layout():
    layout = {}
    for line in LAYOUT_FILE.read_text(encoding="utf-8").splitlines():
        if line.startswith("key_"):
            name, _, value = line[4:].partition(":")
            layout[name] = value
    return layout


def game_running(instance):
    try:
        out = subprocess.run(["powershell", "-NoProfile", "-Command",
                              "Get-CimInstance Win32_Process -Filter \"Name like 'java%'\" | "
                              "Select-Object -ExpandProperty CommandLine"], capture_output=True, text=True).stdout
    except OSError:
        return False
    return instance.name.lower() in out.lower()


def find_instance(args):
    if args:
        return Path(args[0])
    base = Path(os.environ["APPDATA"]) / "PrismLauncher" / "instances"
    cands = sorted(base.glob("cogs-claws-capes*"), key=lambda p: p.stat().st_mtime)
    if not cands:
        raise SystemExit(f"ERROR no cogs-claws-capes instance in {base}")
    return cands[-1]


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    inst = find_instance(args)
    mc = inst / "minecraft"
    opts = mc / "options.txt"
    if not opts.exists():
        raise SystemExit(f"ERROR {opts} not found - launch the instance once first")
    if game_running(inst):
        raise SystemExit("ERROR the game is running. Close Minecraft first (it rewrites options.txt on exit).")

    if "--restore" in argv:
        backups = sorted(mc.glob("options.txt.bak-*"))
        if not backups:
            raise SystemExit("ERROR no backup to restore")
        shutil.copy2(opts, opts.with_name(f"options.txt.before-restore-{datetime.now():%Y%m%d-%H%M%S}"))
        shutil.copy2(backups[-1], opts)
        print(f"{inst.name}: restored {backups[-1].name}")
        return

    layout = load_layout()
    backup = opts.with_name(f"options.txt.bak-{datetime.now():%Y%m%d-%H%M%S}")
    shutil.copy2(opts, backup)
    lines = opts.read_text(encoding="utf-8").splitlines()
    seen = set()
    for i, line in enumerate(lines):
        if line.startswith("key_"):
            name = line[4:].split(":", 1)[0]
            if name in layout:
                lines[i] = f"key_{name}:{layout[name]}"
                seen.add(name)
    for name in layout.keys() - seen:
        lines.append(f"key_{name}:{layout[name]}")
    opts.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{inst.name}: {len(layout)} keys set (backup: {backup.name}; undo with --restore)")
    for k, v in layout.items():
        print(f"  {k:48} {v.replace('key.keyboard.', '')}")
    if "--hold-sprint" in argv:
        dest = mc / "kubejs" / "client_scripts" / "hold_to_sprint.js"
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / "extras" / "hold_to_sprint.js", dest)
        print(f"hold-to-sprint installed: {dest}")


if __name__ == "__main__":
    main(sys.argv[1:])

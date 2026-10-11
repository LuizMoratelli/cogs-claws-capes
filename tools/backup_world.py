"""Back up the server world to another disk (the HUD's "Backup world now" button runs this).

  python tools/backup_world.py [DEST]        default DEST: C:\\Backup\\cogs-claws-capes (the server lives on D:)

- Server STOPPED: zips the world folder now (exact, nothing is writing to it).
- Server RUNNING: a live world is being written, so copying it can tear files. Instead this copies the newest
  Simple Backups zip (made every 2 hours in server/simplebackups) and says how old it is. For a fresh one, type
  `simplebackups backup start` in the server window first, wait for "Backup finished", then press the button.
Keeps the newest 20 zips in DEST.
"""
import shutil
import sys
import time
import zipfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402  (server_running, SERVER)

KEEP = 20


def main():
    dest = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"C:\Backup\cogs-claws-capes")
    server = build.SERVER
    world = server / "world"
    if not world.exists():
        raise SystemExit(f"ERROR no world at {world} - has the server ever been started?")
    dest.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if build.server_running():
        auto = sorted((server / "simplebackups").glob("*.zip"), key=lambda p: p.stat().st_mtime)
        if not auto:
            raise SystemExit("ERROR the server is running and has no Simple Backups zip yet. Type "
                             "`simplebackups backup start` in the server window, wait for it to finish, then retry.")
        src = auto[-1]
        age_min = (time.time() - src.stat().st_mtime) / 60
        out = dest / f"world_{stamp}_from-autobackup.zip"
        shutil.copy2(src, out)
        print(f"Server is running: copied the newest automatic backup ({src.name}, {age_min:.0f} min old).")
        if age_min > 30:
            print("For an up-to-date one: type `simplebackups backup start` in the server window, then press again.")
    else:
        out = dest / f"world_{stamp}.zip"
        files = 0
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for p in world.rglob("*"):
                if p.is_file() and p.name != "session.lock":
                    z.write(p, Path("world") / p.relative_to(world))
                    files += 1
        print(f"Server is stopped: zipped the world now ({files} files).")

    with zipfile.ZipFile(out) as z:  # read back what was written
        bad = z.testzip()
        n = len(z.namelist())
    if bad or n == 0:
        raise SystemExit(f"ERROR backup {out} is damaged ({bad or 'empty'})")
    print(f"OK {out}  ({out.stat().st_size / 1e6:.1f} MB, {n} entries, verified)")

    old = sorted(dest.glob("world_*.zip"), key=lambda p: p.stat().st_mtime)[:-KEEP]
    for p in old:
        p.unlink()
    if old:
        print(f"removed {len(old)} old backup(s), keeping the newest {KEEP}")
    print("Restore: stop the server, rename server\\world to world_old, unzip the backup into server\\ "
          "(it contains a world folder), start the server.")


if __name__ == "__main__":
    main()

# Hosting the server

## Recommendation

**Run it on your own PC and expose it through a playit.gg tunnel.** Your machine (16 threads, 64 GB RAM) is more
than enough for a small group on this pack. Playit makes an **outbound** connection from your PC to its network,
so you **do not open or forward any router port**, your home IP is not shown to players, and players do not install
anything. It is not a Hamachi-style VPN: friends just type an address into Minecraft.

If you want the server online while your PC is off, rent a host instead (see [Option B](#option-b-paid-host)).

| Option | Cost | Up when your PC is off | Router changes | Players install extra software |
|---|---|---|---|---|
| **A. Home PC + playit.gg** | free tier | no | none | no |
| B. Paid Minecraft host | about US$8-28/month for 8 GB | yes | none | no |
| Router port forwarding | free | no | open 25565 to the internet, IP exposed | no |
| Hamachi / ZeroTier / Tailscale | free | no | none | **yes, everyone** |

Port forwarding and the VPN-style tools are the two you said you wanted to avoid. Option A avoids both.

---

## Option A: home PC + playit.gg (step by step)

### 1. Build the server (once, and again after any pack update)

```
cd D:\Projects\cogs-claws-capes
python tools\build.py server
```

This downloads a private Java 17 into `tools\jdk`, installs Forge 47.4.10 into `server\`, downloads the 63 server-side
mods, copies the KubeJS gating scripts and seeds `server\server.properties` with safe defaults. Running it writes
`eula=true`: by running the server you accept the [Minecraft EULA](https://aka.ms/MinecraftEULA).

### 2. First start

Double-click `server\start.bat`. The first boot takes 1-2 minutes. It is ready when the console prints
`Done (...)! For help, type "help"`.

Add people to the whitelist with the helper. It writes the ID the server will really see: a paid account's real ID,
or the offline ID for friends without one. Plain `whitelist add` gets this wrong in offline mode.

```
python tools\whitelist.py add LuizMoratelli --paid
python tools\whitelist.py add FriendWithoutAccount --offline
python tools\whitelist.py list
```

Then in the server console: `whitelist reload`, and once, `op <your name>`.

To shut down, always type `stop` and wait. Do not close the window, or the last minutes of the world may not be saved.

Optional, but it makes exploring much smoother: pre-generate the area around spawn while nobody is online:

```
chunky radius 3000
chunky start
```

### 3. Create the tunnel

1. Download the Windows agent from **https://playit.gg/download** and install it.
2. Run it. It opens a link in your browser: log in or create a free account, then **claim** the agent.
3. On the playit.gg dashboard: **Add tunnel** -> type **Minecraft Java** -> local address `127.0.0.1`, local
   port `25565`.
4. The dashboard shows the public address, something like `name.gl.joinmc.link`. **That is what your friends type.**
   Keep it among your group.

Playit has to be running whenever the server is. You can set it to start with Windows from its tray icon.

### 4. Security checklist (already applied unless noted)

- **Paid and non-paid accounts can both join** (`online-mode=false`), made safe by two mods:
  - **TrueUUID** (client + server) verifies paid accounts with Mojang, so they keep their real ID and skin. A name
    that has logged in verified can never be used offline again (`knownPremiumDenyOffline = true`), and an offline
    player cannot take a name that belongs to a paid account (`allowOfflineForUnknownOnly = true`).
  - **OfflineAuth** (server) makes offline accounts `/register <password> <password>` once and `/login <password>`
    every time. 5 wrong passwords lock the account for 60 s, and players who do not log in within 60 s are kicked.
    Messages are in Portuguese (`config/offlineauth/config.json`).
  - Forgot a password: stop the server, delete that player's entry in `server/config/offlineauth/auth.json`, start it.
- `white-list=true` + `enforce-whitelist=true`: only the people you add can join (use `tools\whitelist.py`, see step 2).
  Even if someone finds the address, they get "You are not white-listed".
- `enable-rcon=false`, `enable-query=false`: no remote admin port.
- **No Windows Firewall rule and no router rule are needed.** Playit's connection is outbound, so do not "allow"
  Java on public networks if Windows asks. Click Cancel.
- Op only yourself. Other players never need op.
- Run the server as your normal Windows user, never "Run as administrator".
- **Backups:** Simple Backups makes a full backup every 2 hours into `server\simplebackups\` and keeps the last 10.
  From time to time, also copy that folder to another disk (for example `D:\Backup`).
- Update mods only through this repo (`build.py lock`, then test a boot), never by dropping random jars into `server\mods`.

### 5. Daily use

1. Start `server\start.bat` and make sure playit is running (tray icon).
2. Friends join with the playit address.
3. When you are done: type `stop`.

---

## Option B: paid host

Pick a host that lets you **upload a custom Forge 1.20.1 modpack** and has a location close to your group (latency
matters more than raw price). For this pack, choose **8 GB RAM** or more. Prices seen on 2026 review sites, which are
affiliate-supported, so check the host's own page before you pay:

- **Bloom.host:** dedicated cores from the 8 GB plans, about US$22 for 8 GB, mountable backups.
- **Sparked Host:** 8 GB from about US$8 (Budget) to US$20.72 (Enterprise). Other packs are uploaded by hand.
- **Apex Hosting:** about US$24-28 for 8 GB, large one-click catalogue.

How to load this pack on any of them:

1. Run `python tools\build.py server` locally.
2. Stop the host's server, choose "Forge 1.20.1-47.4.10" (or "custom jar"), then upload the contents of your local
   `server\` folder **except** `world`, `tools\jdk` and `logs`. The host provides its own Java 17.
3. In the host's panel, set the same `server.properties` values (whitelist on, online-mode on, allow-flight on) and
   8 GB of memory.
4. Start it, run `whitelist add ...` from the panel console, and share the host's address with your friends.

---

## Updating the pack later

```
python tools\build.py lock      # only when you WANT newer mod versions
python tools\scan_hero_recipes.py   # if a hero mod changed
python tools\build.py mrpack    # new client pack for players
python tools\build.py server    # refresh server\mods (your world and server.properties are kept)
```

Then boot the server once and check `server\logs\kubejs\server.log` for `[hero_gating] ... 0 failed` and the
`control ... OK` lines before you hand out the new `.mrpack`. Server and clients must use the **same** pack version.

## Tasks HUD buttons (Scripts tab, group Minecraft)

| Button | What it does |
|---|---|
| Boot Minecraft server | `server\start.bat` in its own window. Type `stop` there to shut down. |
| Rebuild server (update mods/scripts) | `build.py server`. **Refuses while the server runs** (it checks the lock Minecraft holds on `world\session.lock`). Updates mods, KubeJS scripts and the pack-owned `server.properties` keys (`online-mode`, `enforce-secure-profile`, `allow-flight`, `white-list`, `enforce-whitelist`); your other settings and the world are kept. |
| Backup world now | `tools\backup_world.py`: server stopped -> zips the world now; server running -> copies the newest Simple Backups zip (every 2 h) and tells you its age. Goes to `C:\Backup\cogs-claws-capes` (the server is on D:, so a dead disk does not take both), keeps 20, and re-reads each zip after writing. |
| Add friend to whitelist | `tools\add_friend.bat`: asks the name and whether they own Minecraft, writes the right ID. Then `whitelist reload` in the server window. |

**What is in git and what is not:** the pack (mod list + pinned versions), the KubeJS gating, configs, server
settings and all tools are in the repo. The `server\` folder itself (Forge, mod jars, **the world**) is not: it
rebuilds from the repo with `build.py server`, except the world, which is what the backups are for.

## Resetting the world

- **Back to a backup:** stop the server, rename `server\world` to `world_old_<date>`, unzip the backup into `server\`
  (it contains a `world` folder), start.
- **Fresh copy of the same world:** stop the server, rename `server\world` to `world_old_<date>`, start. The seed is
  pinned (`level-seed=8743628307628146557` in `server.properties`, also in `server-overrides/`), so the terrain is the
  same; builds, inventories and XP start over. Whitelist, ops, passwords (`config/offlineauth/auth.json`) and the
  TrueUUID name registry live outside the world folder and are kept.
- Never delete a `world_old_*` folder until you are sure you will not want it back.

## Lag: what it is and what helps (measured 2026-10-11)

- **Server stutter = new terrain.** The log's `Can't keep up! ... ticks behind` warnings (3 of them, 2-10 s, all
  within two minutes of creating the world) come from generating new chunks: Terralith + Biomes O' Plenty + YUNG's
  structures + the dinosaur and boss mods make worldgen heavy. The PC itself was idle (server ~40% of one core, PC 9%).
  **Fix: pre-generate** while nobody is playing, in the server console: `chunky radius 3000` then `chunky start`
  (`chunky pause` / `chunky continue`; progress is printed). Already-generated land costs almost nothing.
- **Memory:** `user_jvm_args.txt` = 8 GB + Aikar's G1 flags (written by `build.py`; it used to be left on JVM defaults
  because a commented `-Xmx4G` in Forge's template fooled the check - fixed).
- **Network (friends only; on this PC `localhost` is 0.3 ms):** the free playit tunnel answered in ~195 ms from here,
  and its IP geolocates to Oregon, US (IP geolocation is approximate). A friend's packets go friend -> relay -> this PC,
  so expect a steady few hundred ms. Same house: use this PC's LAN IP instead. Otherwise check playit's paid plan for
  a region closer to Brazil.
- **Check live:** `spark tps` (server ticks per second, 20 = perfect) and `spark profiler start` / `spark profiler stop`
  (gives a link that shows what is slow).

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

In that console:

```
op YourMinecraftName
whitelist add FriendName1
whitelist add FriendName2
```

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

- `online-mode=true`: only real Mojang/Microsoft accounts can join (no cracked clients pretending to be you).
- `white-list=true` + `enforce-whitelist=true`: only the names you add can join. Even if someone finds the address,
  they get "You are not white-listed".
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

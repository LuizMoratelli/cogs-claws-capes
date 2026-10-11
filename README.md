# Cogs, Claws & Capes

A Minecraft modpack for a private group: **Create** engineering (cogs), **revived dinosaurs** (claws) and
**superheroes you have to earn** (capes), on the community's favourite foundation mods.

| | |
|---|---|
| Minecraft | **1.20.1** |
| Loader | **Forge 47.4.10** (Java 17) |
| Mods | 71 (55 chosen + 16 dependencies), all from Modrinth, pinned in [pack/mods.lock.json](pack/mods.lock.json) |
| Client RAM | 6-8 GB allocated |
| Server RAM | 8 GB (`server/user_jvm_args.txt`) |

**Why 1.20.1:** it is the newest version where all three pillars exist. The superhero ecosystem (Palladium and every
hero pack) and Fossils & Archeology Revival stop at 1.20.1, and Create's largest addon set is there too. The numbers are in
[docs/RESEARCH.md](docs/RESEARCH.md).

## The three pillars

- **Create + addons:** Create 6, Steam 'n' Rails, Crafts & Additions, Enchantment Industry, Deco, Connected,
  Central Kitchen, New Age, Big Cannons, Jetpack, Diesel Generators.
- **Dinosaurs:** Fossils & Archeology Revival (dig fossils, extract DNA, hatch dinosaurs), Alex's Caves (Primordial Caves),
  Alex's Mobs.
- **Superheroes:** Palladium + FSang18's Heroes (hundreds of Marvel/DC suits and powers), Satsu's Iron Man (every Mark,
  suit-up animations), Powerborne Heroes, and **Ben 10**: Alien Evolution (the Omnitrix, aliens unlocked by DNA codes
  found through archaeology) + Omni Extras (more aliens).
- **Foundation:** JEI, Jade, Xaero's maps, Sophisticated Backpacks, Waystones, Farmer's Delight, Supplementaries,
  Comforts, Corpse, Carry On, Iron Chests, Tom's Storage, Open Parties and Claims, YUNG's structures, Biomes O' Plenty,
  Terralith, KubeJS, Simple Backups, plus performance mods (ModernFix, FerriteCore, Embeddium, Entity Culling, ImmediatelyFast).

## Heroes are earned, not crafted on day one

The gating is [overrides/kubejs/server_scripts/hero_gating.js](overrides/kubejs/server_scripts/hero_gating.js):

1. **Hero Core** is made only on a Create **sequenced-assembly** line. You start from a Precision Mechanism, then run
   3 loops of: deploy a **Bio Fossil** (from the dinosaur mod), deploy a **Diamond**, deploy a **Blaze Rod**, press.
   That takes brass-tier Create, fossil hunting and a Nether trip.
2. The **Tailoring Bench**, where every suit is made, needs a **Mechanical Crafter** and a Hero Core.
3. **Every suit** (319 tailoring recipes) costs one more Hero Core.
4. **Every power, serum and gadget** (83 recipes: Compound V, Extremis, spider serum, Iron Man add-ons, the
   **Omnitrix** and its workbench, hero workstations...) leaves the crafting table. Shaped recipes become Create Mechanical Crafting with an extra Hero Core;
   shapeless recipes become heated Create Mixing with a Hero Core.
   Cosmetics (capes, scarves, speed trails, colour variants) and basic parts stay cheap.

The list of targets is generated from the jars by `tools/scan_hero_recipes.py`, so it follows mod updates. The
server prints a self-check on every boot (`logs/kubejs/server.log`, lines `[hero_gating] control ... OK`).

## Docs

- **[docs/PLAYING.md](docs/PLAYING.md):** install the pack and join the server (for every player).
- **[docs/HOSTING.md](docs/HOSTING.md):** run the server safely: home PC + playit.gg tunnel (no port forwarding, no
  Hamachi-style VPN), or a paid host.
- **[docs/RESEARCH.md](docs/RESEARCH.md):** how the version and the mods were chosen, and what the boot tests found.

## Build

Only Python 3 is needed. Java 17 is downloaded into `tools/jdk` by the script.

```
python tools/build.py lock     # re-resolve mods (only when you WANT updates)
python tools/build.py mrpack   # -> dist/cogs-claws-capes-<version>.mrpack  (give this to players)
python tools/build.py server   # -> server/  (Forge + server-side mods + configs + start.bat)
python tools/scan_hero_recipes.py   # after a hero-mod update: regenerate the gating targets
```

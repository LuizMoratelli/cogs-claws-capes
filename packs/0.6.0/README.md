# Cogs, Claws & Capes 0.6.0: Single-player

Minecraft 1.21.1, NeoForge 21.1.262, Java 21.

This is the single-player 0.6 pack. It retains the compatible 0.5 gameplay mods and QoL layer, uses the explicitly documented community ports/replacements where necessary, and expands Create, Aeronautics, electrical engineering and automation. The repository's root 0.5 pack remains separate.

## Install

Download [the Prism import file](dist/cogs-claws-capes-0.6.0-singleplayer.mrpack?raw=true), then use Prism Launcher: Add Instance > Import > Browse and select the downloaded file. Import it as a new instance. Let Prism select Java 21 and use a 6 to 8 GB initial memory allocation, then create a new single-player world. The isolated graphical test uses a 6 GB heap.

The 0.5 server-world copy belongs only to the existing 0.5 instance. Do not open that world in this 1.21.1 pack: several mods and registries differ.

This pack has no dedicated-server package, server installer, authentication mods or server properties. All selected gameplay mods are installed into the client, including mods described as server-side that are needed by the integrated single-player server. The multiplayer client-only exclusion policy from 0.5 is not used here.

## Controls

Hold Shift to run and release it to stop; Ctrl is crouch. The import includes the complete key layout and the client hold-to-sprint script. Backpack, maps, spells, jetpack, Create tools and camera shortcuts are separated; cinematic shortcuts are unbound. See [KEYBINDS.md](docs/KEYBINDS.md) for the layout and intentionally shared equipment controls. Rebuild with `python tools/build.py` to regenerate and validate the layout. Import the rebuilt file into a new Prism instance; existing instances do not update automatically.

## Main additions

- Create: machinery, factories and logistics, with Connected, Copycats+, Steam 'n' Rails community port, Railways Navigator, Big Cannons, Deco, Framed, Bells & Whistles, Interiors, Enchantment Industry, Ore Excavation, Mechanical Extruder, Power Loader, Tweaked Controllers and more.
- Aeronautics + Sable: planes, airships, ground vehicles, Aeroworks, Gadgets & Gizmos, Propulsion: Simulated, Tracks Plus, Ballast, Transmission Linkage, Toolgun and supporting compatibility addons.
- Electrical/industrial: Crafts & Additions, New Age, Diesel Generators, The Factory Must Grow and Electro Energetics. The latter simulates voltage/current and provides an FE converter. Different electrical networks use their own connection/conversion blocks; they are not assumed interchangeable.
- QoL: JEI, Jade, Xaero's minimap and world map, AppleSkin, Mouse Tweaks, Controlling, Crafting Tweaks, Polymorph, Sophisticated Backpacks/Storage, Storage Drawers, Tom's Storage, Carry On and Waystones. Sophisticated Storage's Create integration supports storage on moving contraptions.
- Existing compatible content: Alex's Mobs and Alex's Caves community ports, Ice and Fire Community Edition, Iron's Spellbooks, Cataclysm, Mowzie's Mobs, exploration, farming, building and decoration mods from 0.5.

## Compatibility

See the selection report for every original 0.5 jar, replacement, omission, source URL and pinned version. "Retained" means a compatible version of the project is selected; it does not promise identical content or world-save compatibility.

Palladium and the original hero/Ben 10 stack, Fossils & Archeology, the original Valkyrien Skies/Eureka/Clockwork stack, do not carry over as working original mods. More Mob Variants uses the Renewed community port for this single-player build. That port is not suitable for a dedicated server. Aeronautics/Sable is a different physics system. The custom powered-armor prototype from the earlier experiment is kept separate and is not installed by this pack.

Some included projects only provide prereleases on this target. Those are listed explicitly. Gadgets & Gizmos is kept at stable 1.2.10, rather than the 2.0 prereleases. No shaders/Iris are preinstalled because the current renderer dependency chain conflicts with this pinned Sable setup.

The pack includes seventeen data overrides for Create Framed/Create Deco recipe serialization. Moonlight resource generation uses its supported single-threaded setting to avoid the shutdown hang observed in testing. The old 0.5 Hero Core scripts and old loot patches are not copied blindly across the version change.

## Rebuild

Run `python tools/build.py` from this pack directory. It rebuilds the MRPACK from exact pinned versions and hashes without contacting the version resolver. Add `--verify-downloads` to download/hash-check all locked jars into the ignored local cache. There is no server target.

See the validation report for the checks performed and the outstanding Windows in-game tests.

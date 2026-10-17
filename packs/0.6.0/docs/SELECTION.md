# 0.6 single-player selection and 0.5 carry-over

Checked on 2026-10-17. Target: Minecraft 1.21.1, NeoForge 21.1.262, Java 21. The repository root still builds 0.5 for Forge 1.20.1; this pack is separate.

The original 0.5 lock contains 169 top-level jars. The single-player 0.6 lock contains 192 top-level jars with exact version IDs, download URLs and hashes. Dependencies are recalculated for the new target. All selected jars are required on the client because logical server-side gameplay also runs inside a single-player game.

The selection retains every compatible original direct gameplay choice found, with these explicit replacements and omissions. Different versions or replacement projects do not establish identical content or compatibility with an existing world.

## Create, aircraft and electrical additions

| Project | Pinned version | Purpose |
|---|---|---|
| https://modrinth.com/mod/create | 6.0.10+mc1.21.1 | Aesthetic Technology that empowers the Player |
| https://modrinth.com/mod/create-aeronautics | 1.3.2+mc1.21.1 | Build anything from airships to planes and cars! |
| https://modrinth.com/mod/sable | 2.0.6+mc1.21.1 | A library mod for interactive moving block structures, or "sub-levels" |
| https://modrinth.com/mod/createaddition | neoforge-1.21.1-1.6.0 | Create Crafts & Additions extends Create and acts as a bridge between electricity and kinetic energy |
| https://modrinth.com/mod/create-new-age | 1.2.0+mc1.21.1 | Create: New Age is an addon for the Create mod that adds integration with electricity. |
| https://modrinth.com/mod/create-diesel-generators | 1.21.1-1.3.15 | A Create addon that adds compact diesel generators (engines), simple industrial features and crude oil refinery |
| https://modrinth.com/mod/create-tfmg | 1.2.0 | Heavy Engineering & Oil For The Create Mod |
| https://modrinth.com/mod/create-electro-energetics | 1.21.1-1.1.4 | A realistic(-ish) electricity Create addon that focuses on the generation, transmission, distribution and utilization of electric energy. Also electric trains. |
| https://modrinth.com/mod/create-aeroworks | 1.5.0+mc1.21.1 | A collection of addons for Create Aeronautics with blocks such as the gyroscope, joystick, and more! |
| https://modrinth.com/mod/create-aeronautics-gadgets-and-gizmos | 1.2.10 | A create aeronautics addon that adds new ways to control and interact with physics contraptions |
| https://modrinth.com/mod/create-propulsion-simulated | 1.1.5 | Port of Create: Propulsion mod to NeoForge 1.21.1 with support of Sable and Create: Aeronautics |
| https://modrinth.com/mod/create-tracks-plus | 1.0.5 | This mod is a fork of qwxon's Create:Tracks. Add Create:Trackwork style tracks to game. Need Aeronautics to work. |
| https://modrinth.com/mod/create-steam-n-rails-1.21.1 | 0.2.1+neoforge-mc1.21.1 | An unofficial port of Create: Steam 'n' Rails to 1.21.1. |
| https://modrinth.com/mod/copycats | 3.0.9+mc.1.21.1-neoforge | All the copycats you've ever wanted, combined into a single mod! |
| https://modrinth.com/mod/create-connected | 1.3.3-mc1.21.1 | QoL blocks that you wish existed in Create - Highly configurable, disable what you don't need |
| https://modrinth.com/mod/create-big-cannons | 5.11.7 | A Minecraft mod for building large cannons with the Create mod. |
| https://modrinth.com/mod/bellsandwhistles | v0.4.7-1.21.1 | Additions and adornments for the modern Create engineer. Available for both Fabric & Forge! |
| https://modrinth.com/mod/create-enchantment-industry | 2.4.2 | Automatic Enchanting, with Create |
| https://modrinth.com/mod/create-ore-excavation | 1.21.1-1.6.8 | Extract resources using machines powered by Rotational Force |
| https://modrinth.com/mod/create-railways-navigator | 1.21.1-beta-0.10.0-C6 | A Minecraft Create Mod addon that adds several new features related to train navigation, such as improved display boards, a navigator for searching routes, new schedule entries, and more. |
| https://modrinth.com/mod/create-deco | 2.1.3 | Industrial decoration themed around the aesthetics of the Create mod. |
| https://modrinth.com/mod/create-framed | 1.8.2+1.21.1 | A Create mod addon that adds more Framed Glass variants. |
| https://modrinth.com/mod/interiors | 0.6.1 | A complement to the Create mod that adds new furniture. |
| https://modrinth.com/mod/create-goggles | 6.1.1 | Adds Goggle Helmets and Armored Backtanks for Create Mod |
| https://modrinth.com/mod/sophisticated-storage-create-integration | 1.21.1-0.1.23.246 | Full Featured Sophisticated Storage on Create Contraptions |

Community addon selection uses target-filtered Modrinth searches sorted by downloads, plus dependency and runtime checks. Search false positives are excluded. Electricity includes Create rotation/FE conversion, New Age, diesel/oil machinery and Electro Energetics voltage/current simulation with an FE converter. Their different networks are not assumed interchangeable.

## Explicit replacements

| Original | Selected project | Version | Relationship |
|---|---|---|---|
| Iron Chests | https://modrinth.com/mod/upgraded-iron-chests | 1.5 | Different project with related functionality; not a registry/content-equivalent port |
| Embeddium | https://modrinth.com/mod/sodium | mc1.21.1-0.8.13-neoforge | Renderer replacement for the Sable stack |
| Create: Steam 'n' Rails | https://modrinth.com/mod/create-steam-n-rails-1.21.1 | 0.2.1+neoforge-mc1.21.1 | Unofficial community port |
| Alex's Caves | https://modrinth.com/mod/alexs-caves-unofficial-port | 2.0.10 | Unofficial community port |
| Alex's Mobs | https://modrinth.com/mod/alexs-mobs-1.21.1 | 1.22.17 | Unofficial community port |
| Ice and Fire | https://modrinth.com/mod/iceandfire-ce | 2.0 | Unofficial community port |
| More Mob Variants | https://modrinth.com/mod/more-mob-variants-renewed | V1.0.0 | Unofficial community port |
| Nether's Delight | https://modrinth.com/mod/my-nethers-delight | 1.10.4.1 | Different project with related functionality; not a registry/content-equivalent port |

The original Iron Chests 16.0.7 NeoForge jar explicitly declares Minecraft `[1.21,1.21.1)`, which excludes 1.21.1. It is not force-loaded. The Alex ports use their required Citadel port: https://modrinth.com/mod/citadel-1.21.1-port

## Original gameplay choices without a working carry-over

| Original project | Result |
|---|---|
| Fossils and Archeology: Revival | No original-project published NeoForge 1.21.1 build. A source fork has no downloadable releases in its releases endpoint: https://github.com/BM-Velvet/FossilsArcheologyRevival-1.21.1. Alex's Caves still supplies dinosaur content; Jurassic Reborn was not silently substituted. |
| Palladium | No released original-project NeoForge 1.21.1 build was found. The Palladium hero/Ben 10 stack is not transplanted to a different framework. |
| FSang18's Heroes | No released original-project NeoForge 1.21.1 build was found. The Palladium hero/Ben 10 stack is not transplanted to a different framework. |
| Satsu Iron man addon (Palladium) | No released original-project NeoForge 1.21.1 build was found. The Palladium hero/Ben 10 stack is not transplanted to a different framework. |
| Powerborne Heroes | No released original-project NeoForge 1.21.1 build was found. The Palladium hero/Ben 10 stack is not transplanted to a different framework. |
| Alien Evolution | No released original-project NeoForge 1.21.1 build was found. The Palladium hero/Ben 10 stack is not transplanted to a different framework. |
| Omni Extras: An Alien Evo Addonpack | No released original-project NeoForge 1.21.1 build was found. The Palladium hero/Ben 10 stack is not transplanted to a different framework. |
| Into The Omniverse: AlienEvo AddonPack | No released original-project NeoForge 1.21.1 build was found. The Palladium hero/Ben 10 stack is not transplanted to a different framework. |
| Valkyrien Skies | No original-project NeoForge 1.21.1 release. Aeronautics + Sable is a different physics system and does not convert old ships. |
| Eureka! Ships! for Valkyrien Skies (Forge/Fabric) | No original-project NeoForge 1.21.1 release. Aeronautics provides new vehicle construction, not a port of Eureka ships. |
| Clockwork | No original-project NeoForge 1.21.1 release. Aeronautics provides new vehicle construction, not a port of Clockwork. |

Palladium-related content/support such as PantheonSent, CoreWithStuff, Gravestone: Core and Dampened is not transferred as a functioning superhero stack. Newer Palladium development exists, but this target has no verified released framework. Sources: https://www.curseforge.com/minecraft/mc-mods/threetag-palladium and https://git.threetag.net/ThreeTAG/Palladium

## Intentional single-player exclusions

- TrueUUID and OfflineAuth are multiplayer account-authentication components. They are not installed. This is not a dedicated/offline multiplayer server configuration.
- The earlier custom powered-armor prototype is a separate experiment and is not included in this pack.
- Old 0.5 Hero Core startup items, generated hero targets and hero recipe rewrites depend on missing mods and old serialization. They are not copied. Their old Iron's Spellbooks workstation gating is not preserved.
- Old 0.5 loot patches are not blindly reused against newer mod resources. Only the verified target-specific recipe overrides are supplied.

## Additional candidates excluded by compatibility checks

- Create: Deep Seas pulls an Iris/Sodium dependency chain conflicting with this current Sable lock.
- Aeronautics Encased Fluid Pipes and Throwable Rope Connector pin an older Aeronautics release.
- Big Cannons: Equally Opposite pins a Fabric Sable dependency despite its NeoForge artifact.
- Create Stuff & Additions x Sable compatibility pins an older exact dependency set.
- Bits & Bobs declares incompatibility with the released TFMG version selected here.
- SableCompat supplies a physics-properties resource rejected by the current Sable object schema.
- Copycats+ Aeronautics Weight refers to removed block IDs.
- Dreams & Desires supplies prereleases on this target and is not selected. Create Goggles is an explicitly included beta after the user requested community/QoL additions.
- The inventory-sorter, create-power-grid and create-stuff-netherite-additions slugs returned HTTP 404. This is not a claim that no similarly named project exists elsewhere; no guessed files were installed.

## Target-specific fixes and version policy

- Existing tested compatible pins are retained for the shared matrix; public target release lists were rechecked on 2026-10-17. New addons receive exact pinned versions and hashes.
- Gadgets & Gizmos uses stable 1.2.10 rather than its 2.0 prereleases. Projects without stable target releases, including Create Goggles and Railways Navigator, retain an explicit prerelease status in the lock.
- Dynamic Lights universal-jar metadata lists Fabric-only requirements. Its actual NeoForge descriptor was inspected; those Fabric requirements are not installed.
- Corn Delight accepts newer Farmer's Delight in its embedded descriptor despite its older metadata pin. Farmer's Delight stays at 1.3.4 for Central Kitchen/My Nether's Delight compatibility.
- Iron's Lib 1.21.1-2.x is included for Iron's Spellbooks' embedded requirement.
- Seventeen Create Framed/Create Deco recipes receive pack-level 1.21.1 serialization fixes, without modifying any third-party jar.
- Moonlight uses its supported single-threaded dynamic-generation setting after a resource executor was found to remain alive during shutdown.

## Every 0.5 jar

| Original project | 0.5 version | 0.6 outcome | 0.6 version |
|---|---|---|---|
| 3D Skin Layers (3dskinlayers) | 1.11.3 | Retained | 1.11.3 |
| Alex's Caves (alexs-caves) | 2.0.2 | Replaced by alexs-caves-unofficial-port | 2.0.10 |
| Alex's Mobs (alexs-mobs) | 1.22.9 | Replaced by alexs-mobs-1.21.1 | 1.22.17 |
| Alien Evolution (alienevo) | 1.1.3 | Excluded; see explanation above |  |
| Almanac (almanac) | 1.0.2 | Retained | 1.26.10.2 |
| Amendments (amendments) | 1.20-2.2.6 | Retained | 1.21-2.1.11 |
| Another Furniture (another-furniture) | 3.0.4 | Retained | 4.0.3 |
| AppleSkin (appleskin) | 2.5.1+mc1.20.1 | Retained | 3.0.9+mc1.21 |
| Aquaculture 2 (aquaculture) | 2.5.7 | Retained | 2.7.21 |
| Architectury API (architectury-api) | 9.2.14+forge | Retained | 13.0.11+neoforge |
| Athena (athena-ctm) | 3.1.2 | Retained | 4.0.6 |
| AttributeFix (attributefix) | 21.0.5 | Retained | 21.1.3 |
| Balm (balm) | 7.3.44+forge-1.20.1 | Retained | 21.0.66+neoforge-1.21.1 |
| Better Animations Collection (better-animations-collection) | v8.0.1-1.20.1-Forge | Retained | v21.1.1-1.21.1-NeoForge |
| Better Archeology (better-archeology) | 1.2.1-1.20.1 | Retained | 1.21.1-1.3.9 |
| Better Climbing (better-climbing) | 3-forge | Retained | 4-neoforge |
| Better Combat (better-combat) | 1.9.0+1.20.1-forge | Retained | 2.4.0+1.21.1-neoforge |
| Biomes O' Plenty (biomes-o-plenty) | 18.0.0.592 | Retained | 21.1.0.14 |
| Blueprint (blueprint) | 7.1.5 | Retained | 8.2.0 |
| Bookshelf (bookshelf-lib) | 20.2.15 | Retained | 21.1.81 |
| Buzzier Bees (buzzier-bees) | 6.0.1 | Retained | 7.0.1 |
| Carry On (carry-on) | 2.1.2.7 | Retained | 2.2.6 |
| CC: Tweaked (cc-tweaked) | 1.120.2 | Retained | 1.120.2 |
| Chipped (chipped) | 3.0.7 | Retained | 4.0.2 |
| Chunky (chunky) | 1.3.146 | Retained | 1.4.23 |
| Citadel (citadel) | 2.6.3 | Replaced by citadel-1.21.1-port | 2.7.6 |
| Cloth Config API (cloth-config) | 11.1.136+forge | Retained | 15.0.140+neoforge |
| Clumps (clumps) | 12.0.0.4 | Retained | 19.0.0.1 |
| CMDCam (cmdcam) | 2.2.1 | Retained | 2.2.9 |
| Comforts (comforts) | 6.4.0+1.20.1 | Retained | 9.0.5+1.21.1 |
| Controlling (controlling) | 12.0.2 | Retained | 19.0.5 |
| Create: Copycats+ (copycats) | 3.0.10+mc.1.20.1-forge | Retained | 3.0.9+mc.1.21.1-neoforge |
| CoreWithStuff (corewithstuff) | 1.6-Fix | No matching original target release |  |
| Corn Delight (corn-delight) | 1.2.11-1.20.1 | Retained | 1.2.10-1.21.1 |
| Corpse (corpse) | forge-1.20.1-1.0.23 | Retained | neoforge-1.21.1-1.1.21 |
| Crafting Tweaks (crafting-tweaks) | 18.2.9+forge-1.20.1 | Retained | 21.1.11+neoforge-1.21.1 |
| Create (create) | mc1.20.1-6.0.8 | Retained | 6.0.10+mc1.21.1 |
| Create Big Cannons (create-big-cannons) | 5.11.4 | Retained | 5.11.7 |
| Create: Central Kitchen (create-central-kitchen) | 1.5.1 | Retained | 2.6.2b |
| Clockwork (create-clockwork) | 1.20.1-forge-0.5.6 | Excluded; see explanation above |  |
| Create Confectionery (create-confectionery) | 1.1.3 | Retained | 1.1.3.b |
| Create: Connected (create-connected) | 1.2.3-mc1.20.1 | Retained | 1.3.3-mc1.21.1 |
| Create Deco (create-deco) | 2.0.3-1.20.1-forge | Retained | 2.1.3 |
| Create: Diesel Generators (create-diesel-generators) | 1.20.1-1.3.12 | Retained | 1.21.1-1.3.15 |
| Create Encased (create-encased) | 1.8-ht2 | Retained | 1.21.1-1.9.0-ht3 |
| Create: Enchantment Industry (create-enchantment-industry) | 1.4.1 | Retained | 2.4.2 |
| Create Jetpack (create-jetpack) | 4.4.6 | Retained | 5.2.1 |
| Create: Liquid Fuel (create-liquid-fuel) | 2.2.0-1.20.1 | Retained | 3.0.0-1.21.1 |
| Create Mechanical Extruder (create-mechanical-extruder) | 1.20.1-1.6.11-6.0.6 | Retained | 1.21.1-2.2.2-6.0.10 |
| Create: New Age (create-new-age) | 1.2.0+mc1.20.1 | Retained | 1.2.0+mc1.21.1 |
| Create Ore Excavation (create-ore-excavation) | 1.20.1-1.6.6 | Retained | 1.21.1-1.6.8 |
| Create: Power Loader (create-power-loader) | 2.0.3-mc1.20.1 | Retained | 2.0.5-mc1.21.1 |
| Create Railways Navigator (create-railways-navigator) | 1.20.1-beta-0.10.0-C6 | Retained | 1.21.1-beta-0.10.0-C6 |
| Create: Steam 'n' Rails (create-steam-n-rails) | 1.7.3+forge-mc1.20.1 | Replaced by create-steam-n-rails-1.21.1 | 0.2.1+neoforge-mc1.21.1 |
| Create: Structures Arise (create-structures-arise) | 176.49.49 | Retained | 176.49.49 |
| Create Stuff 'N Additions (create-stuff-additions) | 2.1.2 | Retained | 2.1.4.b |
| Create: Teleporters (create-teleporters) | 2.0.2b | Retained | 3.0.1b |
| Create Crafts & Additions (createaddition) | forge-1.20.1-1.3.3 | Retained | neoforge-1.21.1-1.6.0 |
| CreativeCore (creativecore) | 2.12.40 | Retained | 2.13.51 |
| Curios API (curios) | 5.14.1+1.20.1 | Retained | 9.5.1+1.21.1 |
| Dampened (dampened) | 1.0.2 | No matching original target release |  |
| DragonLib (dragonlib) | 3.0.29+1.20.1-forge | Retained | 3.0.29+1.21.1-neoforge |
| Dynamic Lights (dynamic-lights) | 1.9+mod | Retained | 1.9.3+mod |
| Embeddium (embeddium) | 0.3.31+mc1.20.1 | Replaced by sodium | mc1.21.1-0.8.13-neoforge |
| Enchantment Descriptions (enchantment-descriptions) | 17.1.21 | Retained | 21.1.11 |
| Entity Culling (entityculling) | 1.11.3 | Retained | 1.11.3 |
| Etched (etched) | 3.0.4 | Retained | 5.1.0 |
| Eureka! Ships! for Valkyrien Skies (Forge/Fabric) (eureka) | 1.20.1-forge-1.6.3 | Excluded; see explanation above |  |
| Explorer's Compass (explorers-compass) | 1.20.1-1.4.0-forge | Retained | 1.21.1-3.4.0-neoforge |
| Farmer's Delight (farmers-delight) | 1.20.1-1.3.4 | Retained | 1.21.1-1.3.4 |
| FerriteCore (ferrite-core) | 6.0.1 | Retained | 7.0.3-neoforge |
| Fossils and Archeology: Revival (fossils-and-archeology-revival) | 1.20.1-9.3.4.0-forge | Excluded; see explanation above |  |
| FramedBlocks (framedblocks) | 9.4.3 | Retained | 10.6.3 |
| Freecam (freecam) | 1.2.1+mc1.20.1 | Retained | 1.3.0+mc1.21.1 |
| FSang18's Heroes (fsang18s-heropack) | 12.5.6 | Excluded; see explanation above |  |
| Fusion (Connected Textures) (fusion-connected-textures) | 1.3.16-forge-mc1.20.1 | Retained | 1.3.16-neoforge-mc1.21.1 |
| Fzzy Config (fzzy-config) | 0.7.7+1.20.1+forge | Retained | 0.7.7+1.21+neoforge |
| Geckolib (geckolib) | 4.8.4 | Retained | 4.9.3 |
| Grappling Hook Mod (grappling-hook-mod) | v13-1.20.1 | Retained | 1.21.1-v13 |
| Gravestone: Core (gravestone-core) | 1.2.6 | No matching original target release |  |
| Handcrafted (handcrafted) | 3.0.6 | Retained | 4.0.3 |
| Ice and Fire (ice-and-fire-dragons) | 2.1.13-1.20.1-beta-5 | Replaced by iceandfire-ce | 2.0 |
| ImmediatelyFast (immediatelyfast) | 1.5.5+1.20.4-forge | Retained | 1.6.15+1.21.1-neoforge |
| Immersive Paintings (immersive-paintings) | 0.6.13+1.20.1 | Retained | 0.7.9+1.21.1 |
| Create: Interiors (interiors) | 1.20.1-forge-0.6.0 | Retained | 0.6.1 |
| Into The Omniverse: AlienEvo AddonPack (into-the-omniverse) | 1.0.6 | Excluded; see explanation above |  |
| Iron Chests (iron-chests) | 1.20.1-14.4.4 | Replaced by upgraded-iron-chests | 1.5 |
| Iron's Lib (irons-lib) | 1.20.1-2.2.0 | Retained | 1.21.1-2.2.0 |
| Iron's Spells 'n Spellbooks (irons-spells-n-spellbooks) | 1.20.1-3.16.3 | Retained | 1.21.1-3.16.3 |
| Jade 🔍 (jade) | 11.13.3+forge | Retained | 15.10.6+neoforge |
| Just Enough Items (JEI) (jei) | 15.62.0.219 | Retained | 19.51.0.418 |
| Just Enough Resources (JER) (just-enough-resources-jer) | 1.4.0.247 | Retained | 1.6.0.17 |
| Kotlin for Forge (kotlin-for-forge) | 4.12.0 | Retained | 5.12.0 |
| KubeJS (kubejs) | 2001.6.5-build.26+forge | Retained | 2101.7.2-build.377 |
| KubeJS Create (kubejs-create) | 2001.3.0-build.8+forge | Retained | 2101.3.1-build.18 |
| L_Ender's Cataclysm (l_enders-cataclysm) | 3.31 | Retained | 3.33 |
| Lionfish-API (lionfish-api) | 3.0 | Retained | 3.1 |
| Let Me Despawn (lmd) | 1.5.0 | Retained | 1.26.10.1 |
| Lodestone (lodestonelib) | 1.20.1-1.6.4.1 | No longer a separate dependency of the selected graph |  |
| Lootr (lootr) | 0.7.35.94 | Retained | 1.21.1-1.11.38.127 |
| Macaw's Bridges (macaws-bridges) | 3.1.2 | Retained | 3.1.2 |
| Macaw's Doors (macaws-doors) | 1.1.5 | Retained | 1.1.5 |
| Macaw's Fences and Walls (macaws-fences-and-walls) | 1.2.1 | Retained | 1.2.1 |
| Macaw's Furniture (macaws-furniture) | 3.4.1 | Retained | 3.4.1 |
| Macaw's Lights and Lamps (macaws-lights-and-lamps) | 1.1.5 | Retained | 1.1.5 |
| Macaw's Roofs (macaws-roofs) | 2.3.2 | Retained | 2.3.2 |
| Macaw's Trapdoors (macaws-trapdoors) | 1.1.5 | Retained | 1.1.5 |
| Macaw's Windows (macaws-windows) | 2.4.2 | Retained | 2.4.2 |
| MezzConfig (mezzconfig) | 0.6.8 | No longer a separate dependency of the selected graph |  |
| Mysterious Mountain Lib (mmlib) | 1.6.34-1.20.1 | Retained | 1.2.15-1.21.1 |
| ModernFix (modernfix) | 5.27.88+mc1.20.1 | Retained | 5.27.26+mc1.21.1 |
| Moonlight Lib (moonlight) | 1.20-2.16.36-forge | Retained | 1.21.1-3.7.2 |
| More Hitboxes (more-hitboxes) | 1.20.1-1.9.2-forge | No longer a separate dependency of the selected graph |  |
| More Mob Variants (more-mob-variants) | 1.3.0.1 | Replaced by more-mob-variants-renewed | V1.0.0 |
| Mouse Tweaks (mouse-tweaks) | 1.20.1-2.25.1-forge | Retained | 1.21-2.26.1-neoforge |
| Mowzie's Mobs (mowzies-mobs) | 1.8.2 | Retained | 1.8.2 |
| Naturalist (naturalist) | 5.0pre2 | Retained | 2.0.5+1.21.1-neoforge |
| Nature's Compass (natures-compass) | 1.20.1-1.12.0-forge | Retained | 1.21.1-3.4.0-neoforge |
| Neruina - Ticking Entity Fixer (neruina) | 2.1.1-forge+1.20.1 | Retained | 3.3.4 |
| Nether's Delight (nethers-delight) | 1.20.1-4.0 | Replaced by my-nethers-delight | 1.10.4.1 |
| Not Enough Animations (not-enough-animations) | 1.12.6 | Retained | 1.12.6 |
| OfflineAuth (offlineauth) | 1.0.3 | Not included: multiplayer authentication |  |
| Ok Zoomer - It's Zoom! (ok-zoomer) | 5.4.0-beta.9+forge | Retained | 10.0.0-beta.13+neo |
| Omni Extras: An Alien Evo Addonpack (omni-extras) | 1.0.7.3 | Excluded; see explanation above |  |
| Open Parties and Claims (open-parties-and-claims) | forge-1.20.1-0.32.7 | Retained | neoforge-1.21.1-0.32.7 |
| Packet Fixer (packet-fixer) | 3.3.2 | No longer a separate dependency of the selected graph |  |
| PantheonSent (pantheonsent) | 1.1.1+1.20.1-forge | No matching original target release |  |
| Paragliders (paragliders) | 20.1.3 | Retained | 21.1.5 |
| Pehkui (pehkui) | 3.8.2+1.20.1-forge | No longer a separate dependency of the selected graph |  |
| playerAnimator (playeranimator) | 1.0.2-rc1+1.20-forge | Retained | 2.0.4+1.21.1-forge |
| Polymorph (polymorph) | 0.49.11+1.20.1 | Retained | 1.1.0+1.21.1 |
| Powerborne Heroes (powerborne-heroes) | 0.5.1 | Excluded; see explanation above |  |
| Productive Bees (productivebees) | 1.20.1-12.6.0 | Retained | 1.21.1-13.13.0 |
| Puzzles Lib (puzzles-lib) | 8.1.36 | Retained | 21.1.64 |
| Rechiseled (rechiseled) | 1.2.6-forge-mc1.20.1 | Retained | 1.2.6-neoforge-mc1.21 |
| Rechiseled: Create (rechiseled-create) | 1.1.1-forge-mc1.20 | Retained | 1.1.1-neoforge-mc1.21 |
| Resourceful Lib (resourceful-lib) | 2.1.29 | Retained | 3.0.12 |
| Rhino (rhino) | 2001.2.3-build.10+forge | Retained | 2101.2.7-build.85+Rhino-1.21 |
| Ritchie's Projectile Library (rpl) | 2.1.1 | Retained | 2.1.2 |
| Satsu Iron man addon (Palladium) (satsu-iron-man-addon) | 3.6.2 | Excluded; see explanation above |  |
| Searchables (searchables) | 1.0.3 | Retained | 1.0.2 |
| Shoulder Surfing Reloaded (shoulder-surfing-reloaded) | 1.20.1-5.2.0+forge | Retained | 1.21.1-5.2.0+neoforge |
| Simple Backups (simple-backups) | 1.20.1-3.1.19 | Retained | 1.21-4.0.21 |
| Simply Swords (simply-swords) | 1.70.2-1.20.1 | Retained | 1.70.2-1.21.1 |
| Simply Tooltips (simply-tooltips) | 0.1.5-1.20.1 | Retained | 0.1.5 |
| Create Slice & Dice (slice-and-dice) | 3.6.0 | Retained | 4.3.4 |
| Sophisticated Backpacks (sophisticated-backpacks) | 1.20.1-3.26.12.2206 | Retained | 1.21.1-3.26.12.2208 |
| Sophisticated Core (sophisticated-core) | 1.20.1-1.5.9.2391 | Retained | 1.21.1-1.5.13.2404 |
| Sound Physics Remastered (sound-physics-remastered) | forge-1.20.1-1.5.1 | Retained | neoforge-1.21.1-1.5.1 |
| spark (spark) | 1.10.53-forge | Retained | 1.10.124-neoforge-1.21.1 |
| Storage Drawers (storagedrawers) | 1.20.1-12.15.1 | Retained | 1.21.1-13.11.4 |
| SuperMartijn642's Config Lib (supermartijn642s-config-lib) | 1.1.8-forge-mc1.20 | Retained | 1.1.8-neoforge-mc1.21 |
| SuperMartijn642's Core Lib (supermartijn642s-core-lib) | 1.1.25-forge-mc1.20.1 | Retained | 1.1.25-neoforge-mc1.21 |
| Supplementaries (supplementaries) | 1.20-3.1.44-forge | Retained | 1.21.1-4.0.2 |
| TerraBlender (terrablender) | 3.0.1.11 | Retained | 4.1.0.8 |
| Terralith (terralith) | 2.5.4 | Retained | 2.6.2 |
| Palladium (threetag-palladium) | 4.5.9+1.20.1-forge | Excluded; see explanation above |  |
| Tom's Simple Storage Mod (toms-storage) | 1.20-1.7.1 | Retained | 1.21-2.4.2 |
| TorchMaster (torchmaster) | 20.1.9 | Retained | 21.1.13-release |
| TrueUUID (trueuuid) | 1.3.0+forge-1.20.1 | Not included: multiplayer authentication |  |
| Valkyrien Skies (valkyrien-skies) | 1.20.1-forge-2.4.11 | Excluded; see explanation above |  |
| Waystones (waystones) | 14.1.21+forge-1.20.1 | Retained | 21.1.46+neoforge-1.21.1 |
| Xaero's Minimap (xaeros-minimap) | forge-1.20.1-26.6.0 | Retained | neoforge-1.21.1-26.6.0 |
| Xaero's World Map (xaeros-world-map) | forge-1.20.1-1.47.0 | Retained | neoforge-1.21.1-1.47.0 |
| YUNG's API (yungs-api) | 1.20-Forge-4.0.6 | Retained | 1.21.1-NeoForge-5.1.9 |
| YUNG's Better Dungeons (yungs-better-dungeons) | 1.20-Forge-4.0.4 | Retained | 1.21.1-NeoForge-5.1.4 |
| YUNG's Better Mineshafts (yungs-better-mineshafts) | 1.20-Forge-4.0.4 | Retained | 1.21.1-NeoForge-5.1.1 |
| YUNG's Better Strongholds (yungs-better-strongholds) | 1.20-Forge-4.0.3 | Retained | 1.21.1-NeoForge-5.1.3 |
| Ziplines: Rezipped! (ziplines-rezipped) | 1.3.0-1.20.1-forge | Retained | 1.5.3+1.21.1-neoforge |

## Complete selected 0.6 inventory

| Project | Version | Release type | Group |
|---|---|---|---|
| https://modrinth.com/mod/3dskinlayers | 1.11.3 | release | visual |
| https://modrinth.com/mod/alexs-caves-unofficial-port | 2.0.10 | release | dinosaurs |
| https://modrinth.com/mod/alexs-mobs-1.21.1 | 1.22.17 | release | dinosaurs |
| https://modrinth.com/mod/almanac | 1.26.10.2 | release | dependency of lmd |
| https://modrinth.com/mod/amendments | 1.21-2.1.11 | release | blocks_decor |
| https://modrinth.com/mod/another-furniture | 4.0.3 | release | blocks_decor |
| https://modrinth.com/mod/appleskin | 3.0.9+mc1.21 | release | foundation |
| https://modrinth.com/mod/aquaculture | 2.7.21 | release | gameplay |
| https://modrinth.com/mod/architectury-api | 13.0.11+neoforge | release | dependency of better-archeology |
| https://modrinth.com/mod/athena-ctm | 4.0.6 | release | dependency of chipped |
| https://modrinth.com/mod/attributefix | 21.1.3 | release | quality_of_life |
| https://modrinth.com/mod/balm | 21.0.66+neoforge-1.21.1 | release | dependency of waystones |
| https://modrinth.com/mod/bellsandwhistles | v0.4.7-1.21.1 | release | new_create |
| https://modrinth.com/mod/better-advanced-tooltips | 2101.1.0-build.5 | release | dependency of kubejs |
| https://modrinth.com/mod/better-animations-collection | v21.1.1-1.21.1-NeoForge | release | visual |
| https://modrinth.com/mod/better-archeology | 1.21.1-1.3.9 | release | gameplay |
| https://modrinth.com/mod/better-climbing | 4-neoforge | release | exploration |
| https://modrinth.com/mod/better-combat | 2.4.0+1.21.1-neoforge | release | weapons |
| https://modrinth.com/mod/biomes-o-plenty | 21.1.0.14 | beta | foundation |
| https://modrinth.com/mod/blueprint | 8.2.0 | release | dependency of buzzier-bees |
| https://modrinth.com/mod/bookshelf-lib | 21.1.81 | release | dependency of attributefix |
| https://modrinth.com/mod/buzzier-bees | 7.0.1 | release | industry_bees |
| https://modrinth.com/mod/carry-on | 2.2.6 | release | foundation |
| https://modrinth.com/mod/carryon-aeronautics-compat | 1.1.1 | release | aeronautics |
| https://modrinth.com/mod/cc-sable | 1.3.4 | release | aeronautics |
| https://modrinth.com/mod/cc-tweaked | 1.120.2 | alpha | industry_bees |
| https://modrinth.com/mod/chipped | 4.0.2 | release | blocks_decor |
| https://modrinth.com/mod/chunky | 1.4.23 | release | foundation |
| https://modrinth.com/mod/citadel-1.21.1-port | 2.7.6 | release | dependency of alexs-caves-unofficial-port |
| https://modrinth.com/mod/cloth-config | 15.0.140+neoforge | release | dependency of better-combat |
| https://modrinth.com/mod/clumps | 19.0.0.1 | release | foundation |
| https://modrinth.com/mod/cmdcam | 2.2.9 | release | visual |
| https://modrinth.com/mod/comforts | 9.0.5+1.21.1 | release | foundation |
| https://modrinth.com/mod/configurable | 3.5.3 | release | dependency of neruina |
| https://modrinth.com/mod/controlling | 19.0.5 | release | quality_of_life |
| https://modrinth.com/mod/copycats | 3.0.9+mc.1.21.1-neoforge | release | create_addons_2 |
| https://modrinth.com/mod/corn-delight | 1.2.10-1.21.1 | release | gameplay |
| https://modrinth.com/mod/corpse | neoforge-1.21.1-1.1.21 | release | foundation |
| https://modrinth.com/mod/crafting-tweaks | 21.1.11+neoforge-1.21.1 | release | quality_of_life |
| https://modrinth.com/mod/create | 6.0.10+mc1.21.1 | release | create |
| https://modrinth.com/mod/create-aeronautics | 1.3.2+mc1.21.1 | release | aeronautics |
| https://modrinth.com/mod/create-aeronautics-climbable-rope | 2.1.4 | release | aeronautics |
| https://modrinth.com/mod/create-aeronautics-gadgets-and-gizmos | 1.2.10 | release | aeronautics |
| https://modrinth.com/mod/create-aeronautics-physics-gantry | 1.0.3 | release | aeronautics |
| https://modrinth.com/mod/create-aeronautics-portable-engine-liquid-fuel | 2.0.0 | release | aeronautics |
| https://modrinth.com/mod/create-aeronautics-toolgun | 0.3.6 | release | aeronautics |
| https://modrinth.com/mod/create-aeronautics-transmission-linkage | 0.2.8 | release | aeronautics |
| https://modrinth.com/mod/create-aeroworks | 1.5.0+mc1.21.1 | release | aeronautics |
| https://modrinth.com/mod/create-ballast | 0.1.1 | release | aeronautics |
| https://modrinth.com/mod/create-big-cannons | 5.11.7 | release | create |
| https://modrinth.com/mod/create-central-kitchen | 2.6.2b | release | create |
| https://modrinth.com/mod/create-confectionery | 1.1.3.b | release | create_addons_2 |
| https://modrinth.com/mod/create-connected | 1.3.3-mc1.21.1 | release | create |
| https://modrinth.com/mod/create-contraption-terminals | 1.21.1-1.4.0 | release | new_create |
| https://modrinth.com/mod/create-copper-zinc | 2.0.0 | release | new_create |
| https://modrinth.com/mod/create-deco | 2.1.3 | release | create |
| https://modrinth.com/mod/create-design-n-decor | 2.2b | release | new_create |
| https://modrinth.com/mod/create-diesel-generators | 1.21.1-1.3.15 | release | create |
| https://modrinth.com/mod/create-dragons-plus | 1.11.9 | release | dependency of create-enchantment-industry |
| https://modrinth.com/mod/create-electro-energetics | 1.21.1-1.1.4 | release | additional QoL and engineering |
| https://modrinth.com/mod/create-encased | 1.21.1-1.9.0-ht3 | release | create_addons_2 |
| https://modrinth.com/mod/create-enchantment-industry | 2.4.2 | release | create |
| https://modrinth.com/mod/create-factory | 0.7b-1.21.1 | release | new_create |
| https://modrinth.com/mod/create-framed | 1.8.2+1.21.1 | release | new_create |
| https://modrinth.com/mod/create-goggles | 6.1.1 | beta | additional QoL and engineering |
| https://modrinth.com/mod/create-jetpack | 5.2.1 | release | create |
| https://modrinth.com/mod/create-liquid-fuel | 3.0.0-1.21.1 | release | create_addons_2 |
| https://modrinth.com/mod/create-mechanical-extruder | 1.21.1-2.2.2-6.0.10 | release | create_addons_2 |
| https://modrinth.com/mod/create-misc-and-things | 4.1.1 | release | new_create |
| https://modrinth.com/mod/create-new-age | 1.2.0+mc1.21.1 | release | create |
| https://modrinth.com/mod/create-ore-excavation | 1.21.1-1.6.8 | release | create_addons_2 |
| https://modrinth.com/mod/create-pattern-schematics | 2.0.10 | release | new_create |
| https://modrinth.com/mod/create-power-loader | 2.0.5-mc1.21.1 | release | create_addons_2 |
| https://modrinth.com/mod/create-propulsion-simulated | 1.1.5 | release | aeronautics |
| https://modrinth.com/mod/create-radars | 0.4.9.4-1.21.1 | release | new_create |
| https://modrinth.com/mod/create-railways-navigator | 1.21.1-beta-0.10.0-C6 | beta | create_addons_2 |
| https://modrinth.com/mod/create-simulated-additions | 0.2.3 | release | aeronautics |
| https://modrinth.com/mod/create-steam-n-rails-1.21.1 | 0.2.1+neoforge-mc1.21.1 | release | create |
| https://modrinth.com/mod/create-structures-arise | 176.49.49 | release | create_addons_2 |
| https://modrinth.com/mod/create-stuff-additions | 2.1.4.b | release | create_addons_2 |
| https://modrinth.com/mod/create-teleporters | 3.0.1b | release | create_addons_2 |
| https://modrinth.com/mod/create-tfmg | 1.2.0 | release | new_create |
| https://modrinth.com/mod/create-tracks-plus | 1.0.5 | release | aeronautics |
| https://modrinth.com/mod/create-trading-floor | 3.0.16 | release | new_create |
| https://modrinth.com/mod/create-tweaked-controllers | 1.21.1-1.2.7 | release | new_create |
| https://modrinth.com/mod/createaddition | neoforge-1.21.1-1.6.0 | release | create |
| https://modrinth.com/mod/creativecore | 2.13.51 | release | dependency of cmdcam |
| https://modrinth.com/mod/curios | 9.5.1+1.21.1 | release | dependency of l_enders-cataclysm |
| https://modrinth.com/mod/dragonlib | 3.0.29+1.21.1-neoforge | release | dependency of create-railways-navigator |
| https://modrinth.com/mod/dynamic-lights | 1.9.3+mod | release | visual |
| https://modrinth.com/mod/enchantment-descriptions | 21.1.11 | release | quality_of_life |
| https://modrinth.com/mod/entityculling | 1.11.3 | release | performance |
| https://modrinth.com/mod/etched | 5.1.0 | release | gameplay |
| https://modrinth.com/mod/explorers-compass | 1.21.1-3.4.0-neoforge | release | exploration |
| https://modrinth.com/mod/farmers-delight | 1.21.1-1.3.4 | release | foundation |
| https://modrinth.com/mod/ferrite-core | 7.0.3-neoforge | release | performance |
| https://modrinth.com/mod/framedblocks | 10.6.3 | release | blocks_decor |
| https://modrinth.com/mod/freecam | 1.3.0+mc1.21.1 | release | visual |
| https://modrinth.com/mod/fusion-connected-textures | 1.3.16-neoforge-mc1.21.1 | release | dependency of rechiseled |
| https://modrinth.com/mod/fzzy-config | 0.7.7+1.21+neoforge | release | dependency of immersive-paintings |
| https://modrinth.com/mod/geckolib | 4.9.3 | release | dependency of mowzies-mobs |
| https://modrinth.com/mod/glitchcore | 2.1.0.2 | beta | dependency of biomes-o-plenty |
| https://modrinth.com/mod/grappling-hook-mod | 1.21.1-v13 | release | exploration |
| https://modrinth.com/mod/handcrafted | 4.0.3 | release | blocks_decor |
| https://modrinth.com/mod/iceandfire-ce | 2.0 | release | challenge |
| https://modrinth.com/mod/immediatelyfast | 1.6.15+1.21.1-neoforge | release | performance |
| https://modrinth.com/mod/immersive-paintings | 0.7.9+1.21.1 | release | gameplay |
| https://modrinth.com/mod/interiors | 0.6.1 | release | create_addons_2 |
| https://modrinth.com/mod/irons-lib | 1.21.1-2.2.0 | release | required by irons-spells-n-spellbooks |
| https://modrinth.com/mod/irons-spells-n-spellbooks | 1.21.1-3.16.3 | release | magic |
| https://modrinth.com/mod/jade | 15.10.6+neoforge | release | foundation |
| https://modrinth.com/mod/jade-sable-compat | 1.3.0 | release | aeronautics |
| https://modrinth.com/mod/jei | 19.51.0.418 | release | foundation |
| https://modrinth.com/mod/jupiter | 2.3.7-1.21.1-neoforge | release | dependency of iceandfire-ce |
| https://modrinth.com/mod/just-enough-resources-jer | 1.6.0.17 | alpha | quality_of_life |
| https://modrinth.com/mod/kotlin-for-forge | 5.12.0 | release | dependency of create-jetpack |
| https://modrinth.com/mod/kubejs | 2101.7.2-build.377 | release | foundation |
| https://modrinth.com/mod/kubejs-create | 2101.3.1-build.18 | beta | foundation |
| https://modrinth.com/mod/l_enders-cataclysm | 3.33 | release | challenge |
| https://modrinth.com/mod/lionfish-api | 3.1 | release | dependency of l_enders-cataclysm |
| https://modrinth.com/mod/lithium | mc1.21.1-0.15.4-neoforge | release | additional QoL and engineering |
| https://modrinth.com/mod/lithostitched | 1.8.1-neoforge-21.1 | release | dependency of terralith |
| https://modrinth.com/mod/lmd | 1.26.10.1 | release | quality_of_life |
| https://modrinth.com/mod/lootr | 1.21.1-1.11.38.127 | release | gameplay |
| https://modrinth.com/mod/macaws-bridges | 3.1.2 | release | blocks_decor |
| https://modrinth.com/mod/macaws-doors | 1.1.5 | release | blocks_decor |
| https://modrinth.com/mod/macaws-fences-and-walls | 1.2.1 | release | blocks_decor |
| https://modrinth.com/mod/macaws-furniture | 3.4.1 | release | blocks_decor |
| https://modrinth.com/mod/macaws-lights-and-lamps | 1.1.5 | release | blocks_decor |
| https://modrinth.com/mod/macaws-roofs | 2.3.2 | release | blocks_decor |
| https://modrinth.com/mod/macaws-trapdoors | 1.1.5 | release | blocks_decor |
| https://modrinth.com/mod/macaws-windows | 2.4.2 | release | blocks_decor |
| https://modrinth.com/mod/mechanicals-lib | 1.21.1-1.1.6 | release | dependency of create-mechanical-extruder |
| https://modrinth.com/mod/mmlib | 1.2.15-1.21.1 | release | dependency of corn-delight |
| https://modrinth.com/mod/modernfix | 5.27.26+mc1.21.1 | release | performance |
| https://modrinth.com/mod/moonlight | 1.21.1-3.7.2 | release | dependency of supplementaries |
| https://modrinth.com/mod/more-mob-variants-renewed | V1.0.0 | release | gameplay |
| https://modrinth.com/mod/mouse-tweaks | 1.21-2.26.1-neoforge | release | foundation |
| https://modrinth.com/mod/mowzies-mobs | 1.8.2 | release | challenge |
| https://modrinth.com/mod/my-nethers-delight | 1.10.4.1 | release | gameplay |
| https://modrinth.com/mod/naturalist | 2.0.5+1.21.1-neoforge | release | gameplay |
| https://modrinth.com/mod/natures-compass | 1.21.1-3.4.0-neoforge | release | exploration |
| https://modrinth.com/mod/neruina | 3.3.4 | release | quality_of_life |
| https://modrinth.com/mod/not-enough-animations | 1.12.6 | release | visual |
| https://modrinth.com/mod/numismatics | 1.1.0+neoforge-mc1.21.1 | release | new_create |
| https://modrinth.com/mod/ok-zoomer | 10.0.0-beta.13+neo | release | visual |
| https://modrinth.com/mod/open-parties-and-claims | neoforge-1.21.1-0.32.7 | beta | foundation |
| https://modrinth.com/mod/paragliders | 21.1.5 | release | exploration |
| https://modrinth.com/mod/playeranimator | 2.0.4+1.21.1-forge | beta | dependency of better-combat |
| https://modrinth.com/mod/polymorph | 1.1.0+1.21.1 | release | quality_of_life |
| https://modrinth.com/mod/prickle | 21.1.11 | release | dependency of attributefix |
| https://modrinth.com/mod/productivebees | 1.21.1-13.13.0 | release | industry_bees |
| https://modrinth.com/mod/puzzles-lib | 21.1.64 | release | dependency of better-animations-collection |
| https://modrinth.com/mod/rechiseled | 1.2.6-neoforge-mc1.21 | release | blocks_decor |
| https://modrinth.com/mod/rechiseled-create | 1.1.1-neoforge-mc1.21 | release | create_addons_2 |
| https://modrinth.com/mod/resourceful-config | 3.0.11 | release | dependency of better-archeology |
| https://modrinth.com/mod/resourceful-lib | 3.0.12 | release | dependency of handcrafted |
| https://modrinth.com/mod/rhino | 2101.2.7-build.85+Rhino-1.21 | release | dependency of kubejs |
| https://modrinth.com/mod/rpl | 2.1.2 | release | dependency of create-big-cannons |
| https://modrinth.com/mod/sable | 2.0.6+mc1.21.1 | release | aeronautics |
| https://modrinth.com/mod/searchables | 1.0.2 | release | quality_of_life |
| https://modrinth.com/mod/shoulder-surfing-reloaded | 1.21.1-5.2.0+neoforge | release | visual |
| https://modrinth.com/mod/simple-backups | 1.21-4.0.21 | release | foundation |
| https://modrinth.com/mod/simply-swords | 1.70.2-1.21.1 | release | weapons |
| https://modrinth.com/mod/simply-tooltips | 0.1.5 | release | dependency of simply-swords |
| https://modrinth.com/mod/slice-and-dice | 4.3.4 | release | create_addons_2 |
| https://modrinth.com/mod/sodium | mc1.21.1-0.8.13-neoforge | release | performance |
| https://modrinth.com/mod/sophisticated-backpacks | 1.21.1-3.26.12.2208 | release | foundation |
| https://modrinth.com/mod/sophisticated-core | 1.21.1-1.5.13.2404 | release | dependency of sophisticated-backpacks |
| https://modrinth.com/mod/sophisticated-storage | 1.21.1-1.6.7.2184 | release | additional QoL and engineering |
| https://modrinth.com/mod/sophisticated-storage-create-integration | 1.21.1-0.1.23.246 | release | additional QoL and engineering |
| https://modrinth.com/mod/sound-physics-remastered | neoforge-1.21.1-1.5.1 | alpha | visual |
| https://modrinth.com/mod/spark | 1.10.124-neoforge-1.21.1 | release | foundation |
| https://modrinth.com/mod/storagedrawers | 1.21.1-13.11.4 | release | gameplay |
| https://modrinth.com/mod/supermartijn642s-config-lib | 1.1.8-neoforge-mc1.21 | release | dependency of rechiseled |
| https://modrinth.com/mod/supermartijn642s-core-lib | 1.1.25-neoforge-mc1.21 | release | dependency of rechiseled |
| https://modrinth.com/mod/supplementaries | 1.21.1-4.0.2 | release | foundation |
| https://modrinth.com/mod/terrablender | 4.1.0.8 | beta | dependency of biomes-o-plenty |
| https://modrinth.com/mod/terralith | 2.6.2 | release | foundation |
| https://modrinth.com/mod/toms-storage | 1.21-2.4.2 | release | foundation |
| https://modrinth.com/mod/torchmaster | 21.1.13-release | release | gameplay |
| https://modrinth.com/mod/upgraded-iron-chests | 1.5 | release | foundation |
| https://modrinth.com/mod/uranus | 2.4.1 | release | dependency of iceandfire-ce |
| https://modrinth.com/mod/waystones | 21.1.46+neoforge-1.21.1 | release | foundation |
| https://modrinth.com/mod/waystones-sable | 1.0.7 | release | aeronautics |
| https://modrinth.com/mod/xaeros-minimap | neoforge-1.21.1-26.6.0 | release | foundation |
| https://modrinth.com/mod/xaeros-world-map | neoforge-1.21.1-1.47.0 | release | foundation |
| https://modrinth.com/mod/yungs-api | 1.21.1-NeoForge-5.1.9 | release | dependency of yungs-better-dungeons |
| https://modrinth.com/mod/yungs-better-dungeons | 1.21.1-NeoForge-5.1.4 | release | foundation |
| https://modrinth.com/mod/yungs-better-mineshafts | 1.21.1-NeoForge-5.1.1 | release | foundation |
| https://modrinth.com/mod/yungs-better-strongholds | 1.21.1-NeoForge-5.1.3 | release | foundation |
| https://modrinth.com/mod/ziplines-rezipped | 1.5.3+1.21.1-neoforge | release | exploration |

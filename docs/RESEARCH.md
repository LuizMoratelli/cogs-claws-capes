# Research: version, mods, gating, hosting (2026-10-11)

This page records the data and how it was obtained, so the choices can be re-checked or re-run later.

## 1. Which Minecraft version

**Method:** Modrinth API v2, `GET /project/<slug>/version`, grouped by (game version, loader), newest publish date
per group. Queried live on 2026-10-11.

| Mod (pillar) | Newest MC with builds | Note |
|---|---|---|
| Palladium `threetag-palladium` (heroes framework) | **1.20.1** only (forge/neoforge/fabric, 2026-08-23) | `mpalladium` (1.21.x) is an unrelated mod |
| FSang18's Heroes, Satsu's Iron Man, Powerborne, Arrzee's, Legends Superheroes | **1.20.1** | all active in Sep/Oct 2026 |
| Fossils & Archeology Revival | **1.20.1** (2026-06-08) | no 1.21 build |
| Alex's Caves | 1.20.1 (2024-10-26) | final |
| Create | 1.21.1 NeoForge (2026-04) **and** 1.20.1 Forge 6.0.8 (2025-11) | most addons are 1.20.1 |
| Jurassic Reborn | 1.20.1 and 1.21.1 | alternative dino mod, not used |
| Marvel Superheroes (`marvel-superheroes`) | 1.21.1 NeoForge, last update 2025-07 | the only 1.21 hero mod: 44k downloads, inactive |

**Conclusion:** 1.20.1 is the newest version where all three pillars are well supported. On 1.21.1 the superhero
pillar would be a single inactive mod. Forge was chosen over NeoForge on 1.20.1 because every hero pack, F&A and the
Create addons publish Forge builds. Forge `1.20.1-recommended` = **47.4.10** (from
`files.minecraftforge.net/.../promotions_slim.json`).

## 2. Mod selection

Candidates were checked with `cc_check`-style queries (Modrinth `/project/<slug>/version?loaders=["forge"]&game_versions=["1.20.1"]`):
availability, last publish date, downloads and declared client/server side. `pack/pack.json` holds the choice and
`tools/build.py lock` pins exact versions and hashes in `pack/mods.lock.json`.

Hero packs chosen by downloads and activity: FSang18's Heroes (446k, updated 2026-10-05), Satsu's Iron Man (122k,
2026-10-09), Powerborne Heroes (71k, 2026-09-04). Gods & Heroes (Palladium) was skipped because it pulls in Origins.

### Undeclared dependencies (found by booting the server, not by the API)

The first boot failed with a Forge `ModLoadingException`. The Modrinth pages do not list these dependencies:

| Missing modId | Needed by | Modrinth project |
|---|---|---|
| `kotlinforforge` >= 4.3.0 | `flightlib` (bundled by Create Jetpack) | `kotlin-for-forge` |
| `corewithstuff` | Satsu's Iron Man | `corewithstuff` |
| `gravecore` | Satsu's Iron Man | `gravestone-core` (checked: its `META-INF/mods.toml` declares `modId = "gravecore"`) |

They are listed under `undeclared_dependencies` in `pack/pack.json`.

## 3. Hero gating: how it was built and verified

- `tools/scan_hero_recipes.py` reads every `data/*/recipes/*.json` in `server/mods/*.jar` (10,545 recipes).
  Results: **319** Palladium tailoring recipes (`palladium:suit_set_tailoring` / `item_tailoring`), and **88** crafting
  recipes whose output is an END item (an item no other recipe uses as an ingredient), minus cosmetics, tools and ammo.
  The output is `docs/references/data/hero_targets.json` + `overrides/kubejs/server_scripts/generated/hero_targets.js`.
- `hero_gating.js` rewrites them in `ServerEvents.recipes`.
- **KubeJS 6 gotchas found on the way:**
  - `event.forEachRecipe` runs its callback on worker threads, and Rhino then throws `redeclaration of var`.
    Use `event.findRecipes(...)` and loop on the main thread.
  - `findRecipes` returns an immutable Java list. Rhino cannot call `size()`/`get()` on it
    (`MemberBox cannot access ImmutableCollections$ListN`). Wrap it in `new ArrayList(...)`.
  - `event.custom({...create:mechanical_crafting...})` from a JS object fails with "ItemStack 'result' can't be empty".
    The typed `event.recipes.create.mechanical_crafting(Item.of(..), pattern, {k: Ingredient.of(json)})` works.
  - 10 of FSang/Satsu's own recipes produce items those mods never register (vanilla already rejects them, e.g.
    `fsang:necrotech_dna`). These are skipped and counted.
- **Boot evidence** (2026-10-11, last boot): [data/boot-test-2026-10-11.txt](references/data/boot-test-2026-10-11.txt):
  `rewrote 319 tailoring, 51 -> mechanical crafting, 27 -> heated mixing, 10 skipped, 0 failed`, and 7 controls OK,
  including one in each direction: a suit **needs** the Hero Core, and Palladium's `lead_circuit` does **not**.
- Remaining log warnings come from mods' own data (CoreWithStuff and Steam 'n' Rails recipes for items they do not
  register, and one Satsu Mark 48 recipe). They are harmless and not ours to fix.

## 4. Hosting research

- playit.gg: an outbound tunnel agent, so there is no port forwarding and the home IP is hidden. The free tier covers a
  Minecraft tunnel ([teklynk guide](https://www.teklynk.dev/blog/how-to-host-a-game-server-from-your-home-using-playItgg),
  [Pinggy's overview of alternatives](https://pinggy.io/blog/best_playit_gg_alternatives/)). No independent security audit
  was found. The protection here comes from `online-mode` + whitelist, which hold no matter which tunnel is used.
- Paid 8 GB prices (affiliate-supported reviews, conflicting, so confirm on each host's site):
  [itechguides modded hosting 2026](https://www.itechguides.com/best/modded-minecraft-server-hosting/),
  [dathost 2026 rankings](https://dathost.com/blog/top-minecraft-server-hosts-for-modding).

## Not yet verified

- **Client boot.** Only the dedicated server was boot-tested here. The client `.mrpack` uses the same lock, plus
  6 client-only mods (Embeddium, Entity Culling, ImmediatelyFast, Mouse Tweaks, Xaero's x2). It still needs one launch
  in Prism and one join.
- Balance in real play: whether 3 loops per Hero Core feels right. Change `.loops(3)` in `hero_gating.js`.

## 5. Ben 10 (added 2026-10-11, pack 0.2.0)

Modrinth search `ben 10` / `omnitrix` / `alien evo`, filtered to 1.20.1:

| Project | Downloads | Updated | Notes |
|---|---|---|---|
| **Alien Evolution** `alienevo` | 408k | 2026-03-31 | Palladium-based (same framework as our heroes). **Chosen.** |
| **Omni Extras** `omni-extras` | 72k | 2026-02-15 | AlienEvo addon, extra aliens. **Chosen.** |
| Into the Omniverse | 147k | 2026-02-14 | Omniverse expansion; candidate for later |
| Anonimus Ben 10 / Ben 10 Universe | 50k / 32k | 2024 / "no longer updated" | stale, skipped |

AlienEvo's jar holds 25 `minecraft:crafting_shaped` recipes (namespace `alienevo`); the Omnitrix is
`alienevo:prototype_omnitrix` + `alienevo:omnitrix_workbench`. Alien DNA codes come from archaeology loot tables
(`data/alienevo/loot_tables/archaeology/codes_common.json`, `codes_rare.json`). Omni Extras' namespace is `omni_extras`.
Both namespaces were added to `HERO_NS` in `tools/scan_hero_recipes.py`, which now also writes `global.HERO_NAMESPACES`
so `hero_gating.js` no longer keeps its own list. Colour variants (`*_red`, `*_blue`...) and `machined_*`/`*_bar` are
excluded as cosmetic/food. Boot: `rewrote 319 tailoring, 56 -> mechanical crafting, 27 -> heated mixing, 10 skipped,
0 failed`, control `alienevo:prototype_omnitrix: create:mechanical_crafting OK`
([boot-test-2026-10-11-b.txt](references/data/boot-test-2026-10-11-b.txt)).

## 6. Challenge + magic mods (pack 0.3.0, 2026-10-11)

Added: `l_enders-cataclysm` 3.31, `mowzies-mobs` 1.8.2, `ice-and-fire-dragons` 2.1.13-1.20.1-beta-5 (the only 1.20.1
build is a beta), `irons-spells-n-spellbooks` 1.20.1-3.16.3, `into-the-omniverse` 1.0.6. Bosses of Mass Destruction has
no Forge 1.20.1 build; Twilight Forest and Born in Chaos are not on Modrinth under the slugs tried.

Boot findings, each from the server log, with the fix:

| Finding | Cause | Fix |
|---|---|---|
| FATAL `irons_spellbooks requires irons_lib 1.20.1-2..3` | undeclared dependency | added `irons-lib` |
| `Couldn't parse element loot_tables:irons_spellbooks:chests/catacombs/crypt_loot` ("Missing name") | nested `minecraft:loot_table` entry uses the 1.21 key `value` | `overrides/kubejs/data/...` copy with `name` |
| `... chests/citadel/citadel_tomes` ("Unknown type minecraft:set_written_book_pages") | 1.20.5+ loot function | rewritten as `minecraft:set_nbt` written-book NBT, same translated pages |
| `Parsing error loading power fsang_hero:dampened` (`Unknown mob_effect dampened:genetic`) | FSang's dampening needs the Dampened library (not declared) | added `dampened`; error gone |
| `Couldn't load tag aeo:oxygen ... ad_astra:oxygen` | Into the Omniverse's optional Ad Astra compat | none needed |

Remaining ERROR lines after the fixes (340 unique signatures, all present before these mods were added), classified:
CoreWithStuff loot tables and recipes for moon/chromatix blocks it never registers (~150, harmless); Palladium
`packData is null` once per non-addonpack mod it skips (76, harmless); FSang/Satsu powers and recipes for items those
packs no longer register (20 powers, 10 recipes: leftover data, nothing to load); spawn weight 0 (7), one Curios
`necklace` slot, one client-class access on the server. None stop the server or affect gameplay that exists.
Method: `grep "/ERROR]" boot.log`, normalised and diffed against the previous boot's set (`comm -13`).
Gating with Iron's Spells' workstations: `EXTRA_GATED` in `tools/scan_hero_recipes.py`.
Evidence: [boot-test-2026-10-11-c.txt](references/data/boot-test-2026-10-11-c.txt).

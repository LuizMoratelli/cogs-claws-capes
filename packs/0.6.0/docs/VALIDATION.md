# Validation, 2026-10-17

Target: Minecraft 1.21.1, NeoForge 21.1.262, Java 21. This is a single-player pack.

## Package checks

- All 192 selected original download files match their locked SHA-512 hashes.
- MRPACK has 192 unique download entries, correct Minecraft/NeoForge dependencies, and required client installation for every selected file.
- Distribution contains no server package, authentication mods, world saves, temporary validation adapter or custom powered-armor prototype.
- Overrides contain seventeen Create Framed/Create Deco recipe serialization repairs, the supported Moonlight single-threaded resource-generation setting, 287 keybindings and the hold-to-sprint client script.
- The build checks 34 distinct primary shortcuts, Shift sprint/Ctrl crouch and disabled sprint/crouch toggles. Contextual equipment and inventory bindings still intentionally share some keys, as documented in KEYBINDS.md.
- Every one of the 169 original 0.5 lock entries is accounted for in SELECTION.md. Libraries are recalculated, not force-loaded from the older game.

## Runtime checks

A fresh headless common-content test with 191 selected files, before adding More Mob Variants Renewed, completed startup, created a disposable world and shut down successfully with exit code 0. This checks common content and world loading; it does not validate graphics or every gameplay interaction. No dedicated-server distribution is supplied.

The graphical check uses a disposable Linux NeoForge development client, Java 21, a private virtual display and software rendering. More Mob Variants Renewed is included for this single-player check. Development-only NeoForge GameTests and four intentional Neruina crash-test mixins are disabled only in this temporary harness to emulate production behavior. Official download jars and the published lock remain unchanged. The harness is excluded from the pack.

The full 192-file graphical selection joined the integrated single-player world, rendered terrain/player/HUD/minimap, and opened the inventory with JEI showing its item catalog. Screenshots are preserved in this folder as gameplay.png and inventory-jei.png. This is a short startup and UI smoke check, not an exhaustive gameplay test.

Third-party warnings and optional recipe/loot/tag/model errors remain. In particular, Sable reports an unknown Copycats catwalk physics-property block. The pack does not claim zero log errors, exhaustive recipe validation, or a long-running stability/performance test. Windows Prism, GPU drivers, building/flying contraptions, electrical networks and long-term world progression still need normal playtesting.

## Keybinding integration check

The rebuilt package includes all 287 registered mappings from the client. A fresh run loaded 287/287 exactly, including modifier chords, with `toggleSprint=false` and `toggleCrouch=false`. A temporary adapter seeded the client sprint state with its sprint mapping held, released, held and released. The next tick observed sprinting true, false, true and false, respectively, exercising the actual packaged KubeJS callback. This verifies the release-clears-sprint behavior; it does not simulate physical keyboard travel or exhaustively test equipment combinations. Results are preserved in KEYBINDS-CHECK.txt. The adapter is excluded from the distribution.

## 0.5 save copy

The original server world was copied into a new dated save inside the installed 0.5 Prism instance. The source session lock was acquired exclusively during copying and was not copied. Verification compared all copied files by SHA-256. Only the copied level name was changed for the single-player menu; the original compressed level.dat is preserved alongside it. Server playerdata for the active profile was retained. The source world and existing local New World save were preserved.

This copy belongs to Minecraft 1.20.1 / pack 0.5. It is not included in or migrated to 0.6.

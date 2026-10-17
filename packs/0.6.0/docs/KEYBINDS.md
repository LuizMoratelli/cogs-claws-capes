# 0.6 controls

This layout ships inside the MRPACK. It is independent of 0.5 and its superhero keys. Import the rebuilt file into a new Prism instance to receive it. Replacing a download does not update an already-imported instance.

## Movement

**Hold Shift to run. Release Shift to stop running. Ctrl is crouch, also held.** Both accessibility toggle settings are false. The client script `kubejs/client_scripts/hold_to_sprint.js` clears vanilla's latched land-sprint state when the sprint key is released. Double-tapping forward cannot keep land sprint enabled without holding Shift. Swimming retains vanilla behavior, matching the original 0.5 script.

Grappling-hook motor, slow, climb and slide follow Ctrl rather than occupying the new sprint key. Create's Shift modifier and Jade's hold-for-details remain Shift.

## Main shortcuts

| Key | Action |
|---|---|
| O | Backpack |
| I | Curios accessories |
| N | Hold to zoom |
| Semicolon | Swap camera shoulder |
| M / Ctrl+M | World map / world-map settings |
| U / Ctrl+U | Waypoints / death history |
| Numpad decimal | New waypoint |
| Numpad minus / multiply | Minimap settings / enlarged minimap |
| Numpad 6 / divide | Jetpack on/off / hover |
| Numpad 7 / 8 | Backpack upgrades 1 / 2 |
| Numpad 9 | Tom's Storage terminal |
| Numpad 0 through 5 | Jade's existing shortcuts |
| R / Z | Spell wheel / cast spell |
| Ctrl+V | Supplementaries quiver |
| Alt+X / C / Y / B | Cataclysm armor / helmet / chestplate / boots abilities |
| Ctrl+X | Other special ability |
| F4 | Freecam |
| J | Tracks tuning |
| Alt+R | Railway Navigator overlay options |
| Ctrl+G / Ctrl+H | Physics goggles force gizmo / diagram |
| Ctrl+semicolon / Ctrl+J | Physics goggles interactive diagram / edit overlays |
| Ctrl+L / Alt+K | Dungeon configuration / Kubedex |
| Ctrl+right bracket / Ctrl+F8 | Tooltip tab / capture GIF |

## Equipment and vehicle controls

| Key | Context |
|---|---|
| F6 | Tweaked Controllers mouse focus |
| Ctrl+R / Escape | Tweaked Controllers mouse reset / exit |
| F8 | Aeroworks joystick free camera |
| F10 | Climbable Ropes camera lock |
| G | Aeronautics Toolgun menu/rotation, physics-staff rotation, Propulsion rotate mode, depending on the active tool |
| H / Ctrl+Y / X | Mounted dragon fire / strike / descend |
| V / C / B / numpad Enter | TFMG transmission up / down / custom button / engine start |

The cinematic CMDCam shortcuts and creative toolbar save/load shortcuts are unbound. They remain available in Controls if needed.

## Shared contextual controls

The layout removes competing primary shortcuts, rather than unbinding the basic operation of tools. Some entries in Minecraft's Controls screen can still appear duplicated because mods use the same key in separate contexts:

- Left/right/middle mouse remain attack/use/pick in the world and recipe, item or sorting controls in inventory screens. Grappling hooks, cannons, launchers and physics tools keep their normal held-item mouse controls.
- JEI keeps R for recipes, U for uses and its normal inventory modifiers. Ponder keeps W over an item. These share world keys while used in inventory screens.
- Left Alt remains Create's shared tool-menu modifier, Steam 'n' Rails menus, Copycats fill and related tool modifiers. Shoulder Surfing free look and the spell-bar modifier also use Alt.
- Space remains jump and equipment jump/fly actions. Shift/Ctrl retain contextual modifiers. Escape exits active controllers and menus. Arrow/page keys remain camera adjustments or inventory navigation.
- Big Cannons pitch mode, backpack inventory interaction and TFMG downshift use C in their respective equipment interfaces. TFMG upshift and binocular/launcher mode use V. Toolgun's own two G actions intentionally follow its operating state.

These contextual controls have not all been exhaustively exercised together. The startup integration check verifies that every packaged mapping is loaded, plus the Shift release behavior. It does not establish that every possible equipment combination is conflict-free.

## Rebuild

`pack/keybinds.json` is the source layout. `python tools/keybinds.py` validates the movement settings, checks distinct primary shortcuts and generates the minimal `overrides/options.txt`. `python tools/build.py` performs the same check and includes both the options and client script in the import file. No graphics, audio, account, server-list or window preferences are copied from the test instance.

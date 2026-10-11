// Optional, per player: sprint only while the sprint key is HELD (vanilla keeps sprinting after you let go).
// Install: copy into <instance>/minecraft/kubejs/client_scripts/ (tools/fix_keybinds.py does it), then F3+T in game.
ClientEvents.tick(event => {
  const player = Client.player
  if (player == null) return
  if (player.isSprinting() && !Client.options.keySprint.isDown() && !player.isSwimming()) {
    player.setSprinting(false)
  }
})

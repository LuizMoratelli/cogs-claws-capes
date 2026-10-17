ClientEvents.tick(event => {
  const player = Client.player
  if (player == null) return
  // Vanilla latches sprint after release; swimming needs its separate sprint state.
  if (player.isSprinting() && !Client.options.keySprint.isDown() && !player.isSwimming()) {
    player.setSprinting(false)
  }
})

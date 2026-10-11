// Cogs, Claws & Capes - the items that tie the three pillars together.
// Hero Core: made on a Create sequenced-assembly line from a Precision Mechanism, Bio Fossils (dinosaur pillar),
// diamonds and blaze rods. Every hero suit, power and gadget costs one (see server_scripts/hero_gating.js).

StartupEvents.registry('item', event => {
  event.create('hero_core')
    .displayName('Hero Core')
    .texture('minecraft:item/heart_of_the_sea')
    .rarity('epic')
    .glow(true)
    .tooltip('Primal engineering that awakens a hero.')
    .tooltip('Made on a Create sequenced-assembly line.')

  event.create('incomplete_hero_core', 'create:sequenced_assembly')
    .displayName('Incomplete Hero Core')
    .texture('create:item/incomplete_precision_mechanism')
})

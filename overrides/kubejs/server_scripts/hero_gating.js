// priority: -10
// Cogs, Claws & Capes - superheroes are NOT easy.
//
// 1. Hero Core (kubejs:hero_core) is only made by Create sequenced assembly:
//    Precision Mechanism -> 3 loops of [deploy Bio Fossil, deploy Diamond, deploy Blaze Rod, press].
//    So it needs brass-tier Create, fossil hunting and a Nether trip.
// 2. The Palladium Tailoring Bench (where every suit is made) needs a Mechanical Crafter and a Hero Core.
// 3. Every suit tailoring recipe (global.HERO_TAILORING) costs +1 Hero Core.
// 4. Every hero power / gadget / workstation crafting recipe (global.HERO_CRAFT_END_ITEMS) moves off the crafting
//    table: shaped -> Create Mechanical Crafting with an extra Hero Core row, shapeless -> heated Create Mixing + Hero Core.
// The id lists are generated from the jars by tools/scan_hero_recipes.py (generated/hero_targets.js).

const CORE = 'kubejs:hero_core'
const INC = 'kubejs:incomplete_hero_core'

// Vanilla result JSON -> ItemStack (string, or {item, count, nbt}).
function resultOf(res) {
  if (typeof res == 'string') return Item.of(res)
  var stack = Item.of(res.item, res.count || 1)
  return res.nbt ? Item.of(res.item, res.count || 1, res.nbt) : stack
}

ServerEvents.recipes(event => {
  // --- 1. Hero Core
  event.recipes.create.sequenced_assembly([CORE], 'create:precision_mechanism', [
    event.recipes.create.deploying(INC, [INC, 'fossil:fossil_bio']),
    event.recipes.create.deploying(INC, [INC, 'minecraft:diamond']),
    event.recipes.create.deploying(INC, [INC, 'minecraft:blaze_rod']),
    event.recipes.create.pressing(INC, INC)
  ]).transitionalItem(INC).loops(3).id('cogsclawscapes:hero_core')

  // --- 2. Tailoring Bench
  event.remove({ id: 'palladium:tailoring_bench' })
  event.recipes.create.mechanical_crafting('palladium:tailoring_bench', [
    ' S H ',
    'FFFFF',
    'BWWWB',
    'B   B'
  ], {
    S: 'minecraft:shears',
    H: CORE,
    F: '#palladium:fabrics',
    W: '#minecraft:planks',
    B: 'create:brass_ingot'
  }).id('palladium:tailoring_bench')

  // --- 3 + 4. Rewrite the generated targets
  const tailoring = new Set(global.HERO_TAILORING || [])
  const crafting = new Set(global.HERO_CRAFT_END_ITEMS || [])
  let tailored = 0, mech = 0, mixed = 0, failed = 0, broken = 0
  const rewrites = []

  // findRecipes is a plain list walked on this thread (forEachRecipe runs on worker threads, which breaks Rhino).
  var ArrayList = Java.loadClass('java.util.ArrayList')
  var found = new ArrayList(event.findRecipes({ id: new RegExp('^(' + (global.HERO_NAMESPACES || []).join('|') + '):') }))
  for (var n = 0; n < found.size(); n++) {
    var r = found.get(n)
    var id = String(r.getId())
    if (!tailoring.has(id) && !crafting.has(id)) continue
    try {
      var j = JSON.parse(String(r.json.toString()))
      if (tailoring.has(id)) {
        j.ingredients.push({ ingredient: { item: CORE }, count: 1 })
        rewrites.push([id, 'json', j]); tailored++
      } else if (resultOf(j.result).isEmpty()) {
        // The hero pack ships this recipe for an item it never registers (vanilla already rejects it): nothing to gate.
        broken++
      } else if (j.type == 'minecraft:crafting_shaped') {
        var width = 0
        for (var a = 0; a < j.pattern.length; a++) width = Math.max(width, j.pattern[a].length)
        var pattern = []
        for (var b = 0; b < j.pattern.length; b++) {
          if (j.pattern[b].trim().length == 0) continue // blank rows: Create's crafter grid needs none
          pattern.push(j.pattern[b] + ' '.repeat(width - j.pattern[b].length))
        }
        var left = Math.floor((width - 1) / 2)
        pattern.push(' '.repeat(left) + '$' + ' '.repeat(width - left - 1))
        var key = {}
        for (var ch in j.key) key[ch] = Ingredient.of(j.key[ch])
        key['$'] = Ingredient.of(CORE)
        rewrites.push([id, 'mech', resultOf(j.result), pattern, key]); mech++
      } else if (j.type == 'minecraft:crafting_shapeless') {
        var ings = []
        for (var c = 0; c < j.ingredients.length; c++) ings.push(Ingredient.of(j.ingredients[c]))
        ings.push(Ingredient.of(CORE))
        rewrites.push([id, 'mix', resultOf(j.result), ings]); mixed++
      }
    } catch (err) {
      failed++
      console.warn('[hero_gating] could not rewrite ' + id + ': ' + err)
    }
  }

  for (var k = 0; k < rewrites.length; k++) {
    var w = rewrites[k]
    event.remove({ id: w[0] })
    if (w[1] == 'json') event.custom(w[2]).id(w[0])
    else if (w[1] == 'mech') event.recipes.create.mechanical_crafting(w[2], w[3], w[4]).id(w[0])
    else event.recipes.create.mixing(w[2], w[3]).heated().id(w[0])
  }
  console.info(`[hero_gating] targets ${tailoring.size} tailoring + ${crafting.size} crafting; rewrote ` +
    `${tailored} tailoring, ${mech} -> mechanical crafting, ${mixed} -> heated mixing, ${broken} skipped (result item not registered), ${failed} failed`)
})

// Control after load: the rewritten recipes must exist with the new type (prints to logs/kubejs/server.log).
ServerEvents.loaded(event => {
  const rm = event.server.getRecipeManager()
  const check = (id, want) => {
    const opt = rm.byKey(id)
    const got = opt.isPresent() ? String(opt.get().getType()) : 'MISSING'
    console.info(`[hero_gating] control ${id}: ${got} (want ${want}) ${got == want ? 'OK' : 'FAIL'}`)
  }
  check('palladium:tailoring_bench', 'create:mechanical_crafting')
  check('fsang:compound_v', 'create:mixing')
  check('fsang:all_might_young', 'palladium:suit_set_tailoring')
  check('cogsclawscapes:hero_core', 'create:sequenced_assembly')
  check('satsu_iron_man_addon:additamens/emp', 'create:mechanical_crafting')
  check('alienevo:prototype_omnitrix', 'create:mechanical_crafting')
  check('irons_spellbooks:inscription_table', 'create:mechanical_crafting')
  // A suit must now ask for a Hero Core; a plain Palladium part must not (control in both directions).
  const needsCore = id => {
    const opt = rm.byKey(id)
    if (!opt.isPresent()) return 'MISSING'
    const ings = opt.get().getIngredients()
    for (let i = 0; i < ings.size(); i++) if (ings.get(i).test(Item.of(CORE))) return true
    return false
  }
  console.info(`[hero_gating] control fsang:all_might_young needs core: ${needsCore('fsang:all_might_young')} (want true)`)
  console.info(`[hero_gating] control palladium:lead_circuit needs core: ${needsCore('palladium:lead_circuit')} (want false)`)
})

Data fixes shipped as a KubeJS datapack (files here override the same path inside the mod jars).

- `irons_spellbooks/loot_tables/chests/catacombs/crypt_loot.json` - Iron's Spells 1.20.1-3.16.3 writes a nested
  `minecraft:loot_table` entry with the 1.21 key `"value"`; 1.20.1 needs `"name"`. Without this the crypt chest fails to
  load ("Missing name, expected to find a string") and spawns empty.
- `irons_spellbooks/loot_tables/chests/citadel/citadel_tomes.json` - uses `minecraft:set_written_book_pages`, which only
  exists from 1.20.5. Rewritten as `minecraft:set_nbt` with the same translated pages (title "Citadel Tome").
Re-check both after updating Iron's Spells: delete the file here if the mod's own copy loads without the error.

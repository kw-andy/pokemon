

app_name = "poke_project"

router.register('pokedex', PokeIndexCreatureViewset, basename='pokedex')
router.register('pokemon', PokemonViewset, basename='pokemon')
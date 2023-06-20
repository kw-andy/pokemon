from rest_framework import routers

from poke_api.views import (PokeCreatureByAttribViewset, PokemonViewset, PokeCreatureListViewset)

app_name = "poke_api"

router = routers.SimpleRouter()

router.register('pokemons_list', PokeCreatureListViewset, basename='pokemons_list')
router.register('pokemon_by_attrib', PokeCreatureByAttribViewset, basename='pokemon_by_attrib')
router.register('pokemon', PokemonViewset, basename='pokemon')

urlpatterns = router.urls

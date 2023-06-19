
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from poke_api.views import PokeIndexCreatureViewset
from poke_api.views import PokemonViewset

router = routers.SimpleRouter()

router.register('pokedex', PokeIndexCreatureViewset, basename='pokedex')
router.register('pokemon', PokemonViewset, basename='pokemon')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

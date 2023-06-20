from pyexpat import model
from rest_framework.serializers import ModelSerializer

from poke_api.models import PokedexCreature
from poke_api.models import Pokemon

"""
un "serializer" ça converti des objets Python en un flux (ie, JSON),
mais ça ne gère que ça, la conversion d'objets Python en un flux, 
il reste la partie "récupérer les objets Python" 
avec tout ce que ça peut impliquer de vérifications de droits, filtrages, etc. 
et ça c'est le rôle de tes vues
"""


class PokedexCreatureSerializer(ModelSerializer):
    class Meta:
        model = PokedexCreature
        fields = [
            "Poke_Name",
            "Type_1",
            "Type_2",
            "Total",
            "HP",
            "Attack",
            "Defense",
            "Sp_Atk",
            "Sp_Def",
            "Speed",
            "Generation",
            "Legendary",
        ]


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["pokedex_creature_id", "trainer_id", "surname", "level", "experience"]

from pyexpat import model
from rest_framework.serializers import ModelSerializer

from poke_api.models import PokedexCreature
from poke_api.models import Pokemon


class PokedexCreatureSerializer(ModelSerializer):
    class Meta:
        model = PokedexCreature
        fields = [
            "Name",
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

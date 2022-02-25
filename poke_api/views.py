from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

from poke_api.models import PokedexCreature
from poke_api.models import Pokemon
from poke_api.serializers import PokedexCreatureSerializer
from poke_api.serializers import PokemonSerializer


# Create your views here.


class PokeIndexCreatureViewset(ReadOnlyModelViewSet):
    """
    pour avoir un filtre, mettre le mot clé de cette façon dans le
    path : http://127.0.0.1:8000/pokedex/?Generation=1
    """

    serializer_class = PokedexCreatureSerializer

    def get_queryset(self):
        Pokedexqueryset = PokedexCreature.objects.filter()

        Type_1 = self.request.GET.get("Type_1")
        Type_2 = self.request.GET.get("Type_2")
        Generation = self.request.GET.get("Generation")
        Legendary = self.request.GET.get("Legendary")

        if Type_1 is not None:
            Pokedexqueryset = Pokedexqueryset.filter(Type_1=Type_1)
        elif Type_2 is not None:
            Pokedexqueryset = Pokedexqueryset.filter(Type_2=Type_2)
        elif Generation is not None:
            Pokedexqueryset = Pokedexqueryset.filter(Generation=Generation)
        elif Legendary is not None:
            Pokedexqueryset = Pokedexqueryset.filter(Legendary=Legendary)

        return Pokedexqueryset


class PokemonViewset(ModelViewSet):
    """
    http://127.0.0.1/pokemon
    """

    serializer_class = PokemonSerializer

    def get_queryset(self):

        Pokemonqueryset = Pokemon.objects.all()

        return Pokemonqueryset

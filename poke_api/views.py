from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

from poke_api.models import (PokedexCreature, Pokemon)
from poke_api.serializers import (PokedexCreatureSerializer,
                                  PokemonSerializer)


class PokeCreatureListViewset(ReadOnlyModelViewSet):

    serializer_class = PokedexCreatureSerializer
    queryset = PokedexCreature.objects.all()


class PokeCreatureByAttribViewset(ReadOnlyModelViewSet):
    """
    pour avoir un filtre, mettre le mot clé de cette façon dans le
    path : http://127.0.0.1:8000/api/pokemon_by_attrib/?Generation=1
    """
    serializer_class = PokedexCreatureSerializer

    def get_queryset(self):
        queryset = PokedexCreature.objects.filter()

        type_1 = self.request.GET.get("Type_1")
        type_2 = self.request.GET.get("Type_2")
        generation = self.request.GET.get("Generation")
        legendary = self.request.GET.get("Legendary")

        if type_1 is not None:
            queryset = queryset.filter(Type_1=type_1)
        elif type_2 is not None:
            queryset = queryset.filter(Type_2=type_2)
        elif generation is not None:
            queryset = queryset.filter(Generation=generation)
        elif legendary is not None:
            queryset = queryset.filter(Legendary=legendary)

        return queryset


class PokemonViewset(ModelViewSet):
    """
    http://127.0.0.1:8000/api/pokemon
    """

    serializer_class = PokemonSerializer

    def get_queryset(self):

        Pokemonqueryset = Pokemon.objects.all()

        return Pokemonqueryset

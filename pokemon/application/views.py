from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pokemon.application.serializers import PokemonSerializer
from pokemon.application.abstract_factory import PokemonFactory

class PokemonView(APIView):
    
    def get(self, request, name_id):
        try:
            factory = PokemonFactory()
            service = factory.create_service()
            pokemon = service.get_pokemon_abilities(name_id)
            serializer = PokemonSerializer(pokemon)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Pokemon not found"}, status=status.HTTP_404_NOT_FOUND)

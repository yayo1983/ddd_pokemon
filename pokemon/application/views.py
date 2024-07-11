from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from pokemon.application.abstract_factory import PokemonFactory, ServiceFactory
from django_ratelimit.decorators import ratelimit

def ratelimit_error(request, exception=None):
    return JsonResponse({"error": "rate limit exceeded"}, status=429)

class PokemonView(APIView):
    def __init__(self, factory: ServiceFactory = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.factory = factory or PokemonFactory()
    #@ratelimit(key='ip', rate='5/m', method=ratelimit.ALL, block=True)
    def get(self, request, name_id):
        '''
            rate: Definided the throttling rate in '5/m' (5 requests per minute).

            block: If set to True, block the request when the limit is reached; otherwise it just marks the request as limited.
        '''
        try:
            service = self.factory.create_service()
            pokemon = service.get_pokemon_abilities(name_id)
            serializer = self.factory.create_serializer(pokemon)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response(
                {"error": "Pokemon not found"}, status=status.HTTP_404_NOT_FOUND
            )

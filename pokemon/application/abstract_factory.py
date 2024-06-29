from abc import ABC, abstractmethod
from pokemon.domain.services import PokemonService
from pokemon.application.serializers import PokemonSerializer
from pokemon.infrastructure.models import Pokemon


class ServiceFactory(ABC):
    @abstractmethod
    def create_service(self) -> PokemonService:
        pass

    @abstractmethod
    def create_serializer(self, pokemon: Pokemon) -> PokemonSerializer:
        pass

class PokemonFactory(ServiceFactory):
    def create_service(self) -> PokemonService:
        return PokemonService()

    def create_serializer(self, pokemon: Pokemon) -> PokemonSerializer:
        return PokemonSerializer()

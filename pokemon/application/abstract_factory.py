from abc import ABC, abstractmethod
from pokemon.domain.pokemon_service import PokemonService
from pokemon.application.serializers import PokemonSerializer
from pokemon.infrastructure.pokemon_repository import PokemonRepository
from pokemon.infrastructure.models.pokemon_models import PokemonModel


class ServiceFactory(ABC):
    @abstractmethod
    def create_service(self) -> PokemonService:
        pass

    @abstractmethod
    def create_serializer(self, pokemon: PokemonModel) -> PokemonSerializer:
        pass
    
    @abstractmethod
    def create_pokemon_repository(self):
        pass

class PokemonFactory(ServiceFactory):
    def create_service(self) -> PokemonService:
        return PokemonService(self.create_pokemon_repository())

    def create_serializer(self, pokemon: PokemonModel) -> PokemonSerializer:
        return PokemonSerializer(pokemon)
    
    def create_pokemon_repository(self):
        return PokemonRepository()

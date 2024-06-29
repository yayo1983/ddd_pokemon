from abc import ABC, abstractmethod
from pokemon.domain.services import PokemonService

class ServiceFactory(ABC):
    @abstractmethod
    def create_service(self) -> PokemonService:
        pass

class PokemonFactory(ServiceFactory):
    def create_service(self) -> PokemonService:
        return PokemonService()


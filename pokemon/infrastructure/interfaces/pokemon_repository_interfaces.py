from abc import ABC, abstractmethod
from pokemon.infrastructure.models.pokemon_models import PokemonModel

class PokemonRepositoryInterface(ABC):
    
    @abstractmethod
    def get_pokemon_abilities(self, name_id: str) -> PokemonModel:
        pass
    
from abc import ABC, abstractmethod
from pokemon.infrastructure.models.pokemon_models import PokemonModel

class PokemonService(ABC):
    
    @abstractmethod
    def get_pokemon_abilities(self) -> PokemonModel:
        pass
    
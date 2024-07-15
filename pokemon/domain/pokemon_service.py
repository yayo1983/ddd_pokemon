from pokemon.infrastructure.interfaces.pokemon_repository_interfaces import PokemonRepositoryInterface 
from pokemon.infrastructure.models.pokemon_models import PokemonModel


class PokemonService:
    def __init__(self, pokemon_repository: PokemonRepositoryInterface):
        self.pokemon_repository = pokemon_repository
        

    def get_pokemon_abilities(self, name_id: str) -> PokemonModel:
        return self.pokemon_repository.get_pokemon_abilities(name_id)
    
    
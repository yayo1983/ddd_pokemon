import requests
from pokemon.domain.models import Pokemon

class PokemonService:
    def get_pokemon_abilities(name_id: str) -> Pokemon:
        response = requests.get(f"https://pokeapi.co/api/v2/ability/{name_id}")
        if response.status_code != 200:
            raise ValueError("Pokemon not found")
        data = response.json()
        print(data['results'])
        abilities = [ability['name'] for ability in data['results']]
        return Pokemon(name_id=name_id, abilities=abilities)

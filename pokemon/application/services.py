import os
import requests
from pokemon.domain.models import Pokemon
from dotenv import load_dotenv

load_dotenv()

POKEAPI_URL = os.getenv('POKEAPI_URL')

class PokemonService:
    def get_pokemon_abilities(self, name_id: str) -> Pokemon:
        response = requests.get(f"{POKEAPI_URL}{name_id}")
        if response.status_code != 200:
            raise ValueError("Pokemon not found")
        data = response.json()
        print(data['results'])
        abilities = [ability['name'] for ability in data['results']]
        return Pokemon(name_id=name_id, abilities=abilities)

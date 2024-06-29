import os
import requests
from pokemon.infrastructure.models import Pokemon
from dotenv import load_dotenv

load_dotenv()

POKEAPI_URL = os.getenv('POKEAPI_URL')

class PokemonService:
     def get_pokemon_abilities(self, name_id: str) -> Pokemon:
        try:
            response = requests.get(f"{POKEAPI_URL}{name_id}")
            response.raise_for_status()  
            data = response.json()
            abilities = [ability['ability']['name'] for ability in data['abilities']]
            return Pokemon(name_id=name_id, abilities=abilities)
        except requests.exceptions.HTTPError as http_err:
            raise ValueError(f"HTTP error occurred: {http_err}")  
        except requests.exceptions.RequestException as req_err:
            raise ValueError(f"Request error occurred: {req_err}")  
        except KeyError as key_err:
            raise ValueError(f"Unexpected response format: {key_err}")  
        except Exception as e:
            raise ValueError(f"An error occurred: {e}")  

            

    
   
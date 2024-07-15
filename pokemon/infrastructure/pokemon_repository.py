import os
import requests
from pokemon.infrastructure.models.pokemon_models import PokemonModel
from pokemon.infrastructure.interfaces.pokemon_repository_interfaces import PokemonRepositoryInterface
from dotenv import load_dotenv

load_dotenv()


class PokemonRepository(PokemonRepositoryInterface):
    def __init__(self):
        self.poke_api_url = os.getenv("POKEAPI_URL")

    def get_pokemon_abilities(self, name_id: str) -> PokemonModel:
        try:
            response = requests.get(f"{self.poke_api_url}{name_id}", timeout=5)
            if response.status_code != 200:
                raise ValueError(f"An error occurred in status: {response.status_code}")
            data = response.json()
            abilities = [ability["name"] for ability in data["results"]]
            return PokemonModel(name_id=name_id, abilities=abilities)
        except requests.exceptions.HTTPError as http_err:
            raise ValueError(f"HTTP error occurred: {http_err}") from http_err
        except requests.exceptions.RequestException as req_err:
            raise ValueError(f"Request error occurred: {req_err}") from req_err
        except KeyError as key_err:
            raise ValueError(f"Unexpected response format: {key_err}") from key_err
        except Exception as e:
            raise ValueError(f"An error occurred: {e}") from e

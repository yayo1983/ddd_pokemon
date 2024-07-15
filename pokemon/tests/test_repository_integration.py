import os
import unittest
import requests
from pokemon.infrastructure.pokemon_repository import PokemonRepository
from dotenv import load_dotenv

load_dotenv()

POKEAPI_URL = os.getenv("POKEAPI_URL")


class TestPokemonRepositoryIntegration(unittest.TestCase):

    def test_get_pokemon_abilities_integration(self):
        # Configure the name or ID of the Pokémon for the test
        pokemon_name_id = "#0001"

        # Initialize PokemonService
        repository = PokemonRepository()

        try:
            # Make a real request to the external API
            response = requests.get(f"{POKEAPI_URL}{pokemon_name_id}")
            response.raise_for_status()
            data = response.json()

            # Call the method under test
            pokemon = repository.get_pokemon_abilities(pokemon_name_id)

            # Verify that the abilities obtained match those from the API response
            abilities_from_service = pokemon.abilities
            abilities_from_api = [ability["name"] for ability in data["results"]]

            self.assertEqual(abilities_from_service, abilities_from_api)

        except requests.exceptions.HTTPError as http_err:
            self.fail(f"HTTP error occurred during integration test: {http_err}")

        except requests.exceptions.RequestException as req_err:
            self.fail(f"Request error occurred during integration test: {req_err}")

        except KeyError as key_err:
            self.fail(f"Unexpected response format during integration test: {key_err}")

        except Exception as e:
            self.fail(f"An error occurred during integration test: {e}")


if __name__ == "__main__":
    unittest.main()

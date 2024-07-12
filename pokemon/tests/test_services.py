import unittest
from unittest.mock import patch, Mock
from pokemon.domain.services import PokemonService
import requests


class TestPokemonService(unittest.TestCase):

    @patch("pokemon.domain.services.requests.get")
    def test_get_pokemon_abilities_success(self, mock_get):
        # Configure the mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "results": [{"name": "ability1"}, {"name": "ability2"}]
        }
        mock_get.return_value = mock_response

        # Execute the method under test
        service = PokemonService()
        pokemon = service.get_pokemon_abilities("bulbasaur")

        # Verify the result
        self.assertEqual(pokemon.name_id, "bulbasaur")
        self.assertEqual(pokemon.abilities, ["ability1", "ability2"])

    @patch("pokemon.domain.services.requests.get")
    def test_get_pokemon_abilities_http_error(self, mock_get):
        """
        Test case for handling HTTP errors in get_pokemon_abilities.

        Configures mock_get to raise a simulated HTTP error.
        Calls PokemonService.get_pokemon_abilities with 'bulbasaur'.
        Asserts that a ValueError with the expected message is raised.
        """
        # Configure mock to simulate an HTTP error
        mock_get.side_effect = requests.exceptions.HTTPError("HTTP Error occurred")

        # Execute the method under test and verify the exception
        service = PokemonService()
        with self.assertRaises(ValueError) as cm:
            service.get_pokemon_abilities("bulbasaur")
        self.assertIn("HTTP error occurred", str(cm.exception))

    @patch("pokemon.domain.services.requests.get")
    def test_get_pokemon_abilities_request_error(self, mock_get):
        """
        Test case for handling request errors in get_pokemon_abilities.

        Configures mock_get to raise a simulated RequestException.
        Calls PokemonService.get_pokemon_abilities with 'bulbasaur'.
        Asserts that a ValueError with the expected message is raised.
        """
        # Configure mock to simulate a request error
        mock_get.side_effect = requests.exceptions.RequestException(
            "Request Error occurred"
        )

        # Execute the method under test and verify the exception
        service = PokemonService()
        with self.assertRaises(ValueError) as cm:
            service.get_pokemon_abilities("bulbasaur")
        self.assertIn("Request error occurred", str(cm.exception))

    @patch("pokemon.domain.services.requests.get")
    def test_get_pokemon_abilities_unexpected_response_format(self, mock_get):
        """
        Test case for handling unexpected response formats in get_pokemon_abilities.

        Configures mock response to return an empty JSON object unexpectedly.
        Calls PokemonService.get_pokemon_abilities with 'bulbasaur'.
        Asserts that a ValueError with the expected message is raised.
        """
        # Configure mock response to return an unexpected format
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}  # Unexpected response format
        mock_get.return_value = mock_response

        # Execute the method under test and verify the exception
        service = PokemonService()
        with self.assertRaises(ValueError) as cm:
            service.get_pokemon_abilities("bulbasaur")
        self.assertIn("Unexpected response format", str(cm.exception))


if __name__ == "__main__":
    unittest.main()

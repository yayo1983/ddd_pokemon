import unittest
from unittest.mock import patch, MagicMock
from rest_framework.test import APIClient
from rest_framework import status
from pokemon.application.views import PokemonView

class TestPokemonViewIntegration(unittest.TestCase):
    
    @patch('pokemon.application.abstract_factory.PokemonFactory')
    def test_get_pokemon_abilities_integration(self, MockPokemonFactory):
        # Configure the PokemonFactory mock
        mock_factory_instance = MockPokemonFactory.return_value
        mock_service = mock_factory_instance.create_service.return_value
        mock_pokemon = MagicMock()
        mock_pokemon.name_id = 'bulbasaur'
        mock_pokemon.abilities = ['ability1', 'ability2']
        mock_service.get_pokemon_abilities.return_value = mock_pokemon
        
        # Configure the view and make the mock request
        view = PokemonView()
        request = MagicMock()
        request.query_params = {'name_id': 'bulbasaur'}
        
        response = view.get(request, name_id='bulbasaur')
        
        # Check expected behavior
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name_id'], 'bulbasaur')
        self.assertEqual(response.data['abilities'], ['ability1', 'ability2'])
    
    @patch('pokemon.application.abstract_factory.PokemonFactory')
    def test_get_pokemon_abilities_integration_not_found(self, MockPokemonFactory):
        # Configure the Pokemon Factory mock to simulate an unfound Pokemon
        mock_factory_instance = MockPokemonFactory.return_value
        mock_service = mock_factory_instance.create_service.return_value
        mock_service.get_pokemon_abilities.side_effect = ValueError("Pokemon not found")
        
        # Configure the view and make the mock request
        view = PokemonView()
        request = MagicMock()
        request.query_params = {'name_id': 'non_existing_pokemon'}
        
        response = view.get(request, name_id='non_existing_pokemon')
        
        # Check expected behavior
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Pokemon not found')

if __name__ == '__main__':
    unittest.main()

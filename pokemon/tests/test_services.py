import pytest
import requests
from unittest.mock import patch
from pokemon.services import PokemonService

@pytest.fixture
def mock_response():
    return {
        'results': [
            {'name': 'overgrow'},
            {'name': 'chlorophyll'}
        ]
    }

@patch('pokemon.services.requests.get')
def test_get_pokemon_abilities(mock_get, mock_response):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    service = PokemonService()
    pokemon = service.get_pokemon_abilities('bulbasaur')

    assert pokemon.name_id == 'bulbasaur'
    assert pokemon.abilities == ['overgrow', 'chlorophyll']

@patch('pokemon.services.requests.get')
def test_get_pokemon_abilities_not_found(mock_get):
    mock_get.return_value.status_code = 404

    service = PokemonService()

    with pytest.raises(ValueError, match="Pokemon not found"):
        service.get_pokemon_abilities('invalid')

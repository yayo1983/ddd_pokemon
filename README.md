# Pokemon Proxy Project

This project is a Django REST API that acts as a proxy to fetch Pokémon abilities from an external API. It includes a management system for products, with endpoints to create products, manage inventory, and handle orders.

## Features
- Fetch Pokemón abilities from an external API.
To know more about Pokemon services you can read here:
```sh
https://pokeapi.co/docs/v2#abilities
```
and 
```sh
https://bulbapedia.bulbagarden.net/wiki/Hoenn_Route_121
```
For see un example of endpoint
```sh
https://pokeapi.co/api/v2/ability/#0001
```
The list of pokemon
```sh
https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_Ability
```

## Project Structure
```sh
pokemon-proxy/
├── .env
├── .gitignore
├── README.md
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── pyproject.toml
├── poetry.lock
├── pokemon_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pokemon/
│   ├── __init__.py
│   ├── application/
│   │   ├── __init__.py
│   │   │── views.py
│   │   └── serializers.py
│   │   └── abstract_factory.py
│   ├── domain/
│   │   ├── __init__.py
│   │   └── services.py
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── migrations/
│   │   ├── __init__.py
└── tests/
    ├── __init__.py
    └── test_service.py
    └── test_service_integration.py
```

## Installation

1. Create .env and put variable POKEAPI_URL to save value of service URL Pokemon 

2. Install dependencies
```sh
poetry install
```

3. Correr Redis en docker
```sh
docker run -d --name redis-server -p 6379:6379 redis
```

## Run test

All the test 
```sh
poetry run pytest
```
or One specific test file 
```sh
poetry run python manage.py test pokemon.tests.test_service_integration
```

or a specific function in one file test
```sh
poetry run python3 -m unittest pokemon.tests.test_services.TestPokemonService.test_get_pokemon_abilities_success
```
## Run project
```sh
poetry run python manage.py runserver
```

# API Endpoints
## Get Abilities 

- URL: /pokemon/{name_id}/
- Method: GET
- Payload:
```sh
{
  "name_id": "string",
}
```

## Swagger documentation

- URL: swagger/
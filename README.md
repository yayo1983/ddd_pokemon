# Pokemon Proxy Project

This project is a Django REST API that acts as a proxy to fetch Pokémon abilities from an external API. It includes a management system for products, with endpoints to create products, manage inventory, and handle orders.

## Features
- Fetch Pokemón abilities from an external API.

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
│   │   └── services.py
│   ├── domain/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   │── views.py
│   │   └── serializers.py
│   ├── migrations/
│   │   ├── __init__.py
└── tests/
    ├── __init__.py
    └── test_service.py
```

## Installation

1. Create .env and put variable POKEAPI_URL to save value of service URL Pokemon 

2. Install dependencies
```sh
poetry install
```

## Run test
```sh
poetry run pytest
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
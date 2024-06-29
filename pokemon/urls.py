from django.urls import path
from pokemon.application.views import PokemonView


urlpatterns = [
    path("pokemon/<str:name_id>/", PokemonView.as_view(), name="pokemon-detail"),
]

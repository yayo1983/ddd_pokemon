from rest_framework import serializers
from pokemon.domain.models import Pokemon

class PokemonSerializer(serializers.Serializer):
    name_id = serializers.CharField(max_length=100)
    abilities = serializers.ListField(child=serializers.CharField(max_length=100))

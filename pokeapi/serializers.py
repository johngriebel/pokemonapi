from rest_framework import serializers

from .models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["id", "creature_id", "created_at", "updated_at", "name",
                  "primary_type", "secondary_type", "total", "hp", "attack", "defense",
                  "special_attack", "special_defense", "speed", "generation",
                  "legendary"]
        read_only_fields = ["id", "created_at", "updated_at"]

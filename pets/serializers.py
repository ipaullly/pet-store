from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('name', 'age', 'animal_type', 'color', 'created_at', 'updated_at')

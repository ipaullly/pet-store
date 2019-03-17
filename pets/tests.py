import json
from django.test import TestCase, Client
from django.urls import reverse
from .serializers import PetSerializer
from .models import Pet
from rest_framework import status

# Create your tests here.
client = Client()

class PetTest(TestCase):
    """Test module for Pet model"""
    def setUp(self):
        Pet.objects.create(
            name='Otto', age=4, animal_type='Ferret', color='brown and black'
        )
        Pet.objects.create(
            name='Judas', age=1, animal_type='West African bush viper', color='olive green'
        )
    def test_pet_animal_type(self):
        pet_otto = Pet.objects.get(name='Otto')
        pet_judas = Pet.objects.get(name='Judas')
        self.assertEqual(
            pet_otto.get_animal_type(), "Otto is a Ferret."
        )
        self.assertEqual(
            pet_judas.get_animal_type(), "Judas is a West African bush viper."
        )

class CreateNewPetTest(TestCase):
    """Test module for inserting a new puppy"""
    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'age': 4,
            'animal_type': 'Namibian grass snake',
            'color': 'Bronze'
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'animal_type': 'Dwark Hamster',
            'color': 'White'
        }
    def test_create_valid_pet(self):
        response = client.post(
            reverse('get_post_pets'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_pet(self):
        response = client.post(
            reverse('get_post_pets'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
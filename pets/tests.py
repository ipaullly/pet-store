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
    """Test module for inserting a new pet"""
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

class GetAllPetsTest(TestCase):
    """Test module for GET all pets API"""
    def setUp(self):
        Pet.objects.create(
            name='Casper', age=3, animal_type='Caucasian Mountain dog', color='Blonde'
        )
        Pet.objects.create(
            name='Muffin', age=1, animal_type='Guinea Pig', color='Brown'
        )
        Pet.objects.create(
            name='Rambo', age=2, animal_type='Tortoise', color='Black'
        )
        Pet.objects.create(
            name='Ricky', age=6, animal_type='Parrot', color='Pink and Yellow'
        )
    def test_get_all_pets(self):
        # get API response
        response = client.get(reverse('get_post_pets'))
        # get data from db
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSinglePetTest(TestCase):
    
    def setUp(self):
        self.lavender = Pet.objects.create(
            name='Lavender', age=2, animal_type='Koala', color='Grey'
        )
    
    def test_get_valid_single_pet(self):
        response = client.get(
            reverse('get_delete_update_pets', kwargs={'pk': self.lavender.pk})
        )
        pet = Pet.objects.get(pk=self.lavender.pk)
        serializer = PetSerializer(pet)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_pet(self):
        response = client.get(
            reverse('get_delete_update_pets', kwargs={'pk': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class UpdateSinglePetTest(TestCase):
    """Test module for updating an existing pet record"""

    def setUp(self):
        self.demetrius = Pet.objects.create(
            name='Demetrius', age=3, animal_type='Gold fish', color='Orange'
        )
        self.neoptalamus = Pet.objects.create(
            name='Neoptalamus', age=1, animal_type='Siamese cat', color='White'
        )
        self.valid_payload = {
            'name': 'Muffy',
            'age': 2,
            'animal_type': 'Labrador',
            'color': 'Black'
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'animal_type': 'Pamerion',
            'color': 'White'
        }
    def test_valid_update_pet(self):
        response = client.put(
            reverse('get_delete_update_pets', kwargs={'pk': self.neoptalamus.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    def test_invalid_update_pet(self):
        response = client.put(
            reverse('get_delete_update_pets', kwargs={'pk': self.demetrius.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSinglePetTest(TestCase):
    """Test module for deleting an existing pet record"""
    def setUp(self):
        self.demetrius = Pet.objects.create(
            name='Demetrius', age=3, animal_type='Gold fish', color='Orange'
        )
        self.neoptalamus = Pet.objects.create(
            name='Neoptalamus', age=1, animal_type='Siamese cat', color='White'
        )
    def test_valid_delete_pet(self):
        response = client.delete(
            reverse('get_delete_update_pets', kwargs={'pk': self.demetrius.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    def test_invalid_delete_pet(self):
        response = client.delete(
            reverse('get_delete_update_pets', kwargs={'pk': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
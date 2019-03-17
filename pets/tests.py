from django.test import TestCase
from .models import Pet
# Create your tests here.

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
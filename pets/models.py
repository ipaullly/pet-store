from django.db import models

# Create your models here.
class Pet(models.Model):
    """Pet model that defines the attritbutes of the pet"""
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    animal_type = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_animal_type(self):
        return self.name + ' is a ' + self.animal_type + '.'
    def __repr__(self):
        return self.name + ' is added.'

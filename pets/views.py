from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pet
from .serializers import PetSerializer

@api_view(['POST', 'GET'])
def get_post_pets(request):
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'age': int(request.data.get('age')),
            'animal_type': request.data.get('animal_type'),
            'color': request.data.get('color')
        }
        serializer = PetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_delete_update_pets(request, pk):
    try:
        pet = Pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single puppy
    if request.method == 'GET':
        serializer = PetSerializer(pet)
        return Response(serializer.data)
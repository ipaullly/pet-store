from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pet
from .serializers import PetSerializer

@api_view(['POST'])
def get_post_pets(request):
    if request.method == 'POST':
        return Response({})

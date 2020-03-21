from django.shortcuts import render
from rest_framework import viewsets
from .models import Cocktail
from .serializers import CocktailSerializer
from users.models import User
# Create your views here.

class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
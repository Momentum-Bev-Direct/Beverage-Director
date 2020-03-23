from django.shortcuts import render
from rest_framework import viewsets
from .models import Cocktail, Spirit, MiscIngredient, Rating
from .serializers import CocktailSerializer, SpiritSerializer, MiscIngredientSerializer, RatingSerializer, UserSerializer
from users.models import User


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

class SpiritViewSet(viewsets.ModelViewSet):
    queryset = Spirit.objects.all()
    serializer_class = SpiritSerializer

class MiscIngredientViewSet(viewsets.ModelViewSet):
    queryset = MiscIngredient.objects.all()
    serializer_class = MiscIngredientSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
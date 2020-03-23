from django.shortcuts import render
from rest_framework import viewsets
from .models import Cocktail
from .serializers import CocktailSerializer
from users.models import User
from config import urls
# Create your views here.

class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

def base_launch(request):
    return render(request, 'base.html')

def drink_builder(request):
    return render(request, 'core/drink_builder.html')
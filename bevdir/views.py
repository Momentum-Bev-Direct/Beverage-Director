from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Cocktail, Spirit, MiscIngredient, Rating, Shot, Portion
from .serializers import CocktailSerializer, SpiritSerializer, MiscIngredientSerializer, RatingSerializer, UserSerializer, ShotSerializer, PortionSerializer
from users.models import User
from config import urls
import json
import requests
from bs4 import BeautifulSoup


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
    def get_queryset(self):
        user = self.request.user


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


class ShotViewSet(viewsets.ModelViewSet):
    queryset = Shot.objects.all()
    serializer_class = ShotSerializer


class PortionViewSet(viewsets.ModelViewSet):
    queryset = Portion.objects.all()
    serializer_class = PortionSerializer

def welcome_page(request):
    if request.user.is_authenticated:
        return homepage(request)
    else:
        return render(request, 'bevdir/welcome.html')

def homepage(request):
    cocktails =  Cocktail.objects.filter(user=request.user)
    cocktails_dataset = []

    for cocktail in cocktails:
        cocktail_dict = {}
        cocktail_dict["id"]=cocktail.pk
        cocktail_dict["name"]= cocktail.name
        cocktail_dict["target"]= cocktail.target_profit

        cocktail_dict["shots"]= {
            str(shot.pk):{"volume":shot.volume, "cost": shot.cost, "brandname": shot.spirit.brandname} for shot in cocktail.shots.all()
        }

        cocktail_dict["portions"]= {
            str(portion.pk):{"amount": portion.amount, "cost": portion.cost, "name": portion.misc_ingredient.name} for portion in cocktail.portions.all()
        }

        cocktails_dataset.append(cocktail_dict)

    context= {}
    context["cocktails"]=json.dumps(cocktails_dataset)
    return render(request, 'bevdir/home.html', context)

def edit_cocktail(request, pk):
    cocktail = get_object_or_404(Cocktail, pk=pk)
    cocktail_dict = {}
    cocktail_dict["id"]=cocktail.pk
    cocktail_dict["name"]= cocktail.name
    cocktail_dict["target"]= cocktail.target_profit

    cocktail_dict["shots"]= [{"id": shot.pk, "volume":shot.volume, "cost": shot.spirit.price_per_oz, "brandname": shot.spirit.brandname} for shot in cocktail.shots.all()]

    cocktail_dict["portions"]= [{"id": portion.pk, "amount": portion.amount, "unit": portion.unit, "cost": portion.price_per_unit, "name": portion.misc_ingredient.name} for portion in cocktail.portions.all()]

    spirits = Spirit.objects.all()
    spirit_dict= []
    for spirit in spirits:
        spirit_dict.append({"id": spirit.pk, "brandname": spirit.brandname, "cost": spirit.price_per_oz, "category": spirit.category})

    context = {}
    context['cocktail']=json.dumps(cocktail_dict)
    context['spirits']=json.dumps(spirit_dict)
    return render(request, 'bevdir/drink_builder_edit.html', context=context)

def base_launch(request):
    cocktails = Cocktails.object.all()
    return render(request, 'base.html', {'cocktails': cocktails })

def drink_builder(request):
    return render(request, 'bevdir/drink_builder.html')





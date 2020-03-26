from django.shortcuts import render, redirect
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


def homepage(request):
    # cocktails = Cocktail.objects.all()
    # cocktails_dataset = [{
    #     "id": cocktail.pk,
    #     "name":cocktail.name,
    #     "total_cost":cocktail.total_cost,
    #     "recommended_price":cocktail.recommended_price
    #     } for cocktail in cocktails]
    # context= {}
    # context["cocktails"]=json.dumps(cocktails_dataset)
    return render(request, 'bevdir/home.html')

def base_launch(request):
    cocktails = Cocktails.object.all()
    return render(request, 'base.html', {'cocktails': cocktails })

def drink_builder(request):
    return render(request, 'bevdir/drink_builder.html')


def populate_spirits(request):
    response = requests.get("https://abc.nc.gov/Pricing/PriceList")
    soup = BeautifulSoup(response.text, 'html.parser')
    spirits = soup.find_all(class_="list-generic")
    for spirit in spirits:
        elements = spirit.find_all('div')
        try:
            this_spirit = Spirit.objects.get(brandname=elements[2].get_text())
            this_spirit.mxb = float(elements[7].get_text().replace('$', '').replace(',',''))
            this_spirit.save()
        except Spirit.DoesNotExist:
            new_spirit = Spirit.objects.create(
                nc_code = elements[0].get_text(),
                supplier = elements[1].get_text(),
                brandname = elements[2].get_text(),
                proof = elements[4].get_text(),
                size = float(elements[5].get_text().replace('M', '').replace('L', '').replace(',','')),
                mxb = float(elements[7].get_text().replace('$', '').replace(',',''))
            )
            new_spirit.save()
    return redirect('homepage')


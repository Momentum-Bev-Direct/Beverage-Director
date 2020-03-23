from rest_framework import serializers
from .models import Cocktail, Spirit, MiscIngredient, Rating
from users.models import User

class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SpiritSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spirit
        fields = '__all__'

class MiscIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiscIngredient
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

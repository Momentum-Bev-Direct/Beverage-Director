from rest_framework import serializers
from users.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'password')
    extra_kwargs = {'password': { 'required':True, 'write_only':True}}

    def create(self, validated_data):
      user = User.objects.create_user(**validated_data)
      Token.objects.create(user=user)
      return user

# NEED THESE SETTINGS: 

  INSTALLED_APPS = [
    'rest_framework.authtoken',
  ]

REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES': {
      'rest_framework.permissions.IsAuthenticated'
  }
}

# MODELVIEWS:

from rest_framework import viewsets, status
from rest_framework.response import Response 
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

class GeneralModelViewSet(viewsets.ModelViewSet):
  queryset = #yadda yadda
  serializer_class = #yadda yadda 
  authentication_classes = (TokenAuthentication)
  permission_classes = (AllowAny)

  
#SCRAPING
#Beautiful Soup
#Look up management commands. 

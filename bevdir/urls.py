from . import views
from rest_framework import routers
from django.urls import include, path


router = routers.DefaultRouter()
router.register('cocktail', views.CocktailViewSet)
router.register('spirit', views.SpiritViewSet)
router.register('misc', views.MiscIngredientViewSet)
router.register('rating', views.RatingViewSet)
router.register('user', views.UserViewSet)
router.register('shot', views.ShotViewSet)
router.register('portion', views.PortionViewSet)

urlpatterns = [
    path('', include(router.urls),),


]

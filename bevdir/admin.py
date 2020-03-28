from django.contrib import admin
from .models import Spirit, Cocktail, Shot, Portion
# Register your models here.

admin.site.register(Spirit)
admin.site.register(Cocktail)
admin.site.register(Shot)
admin.site.register(Portion)
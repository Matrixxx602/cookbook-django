from django.contrib import admin
from .models import Recipe, Allergen

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Allergen)
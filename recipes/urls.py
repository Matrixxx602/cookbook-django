from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/details/<int:id>', views.details, name='details'),
]
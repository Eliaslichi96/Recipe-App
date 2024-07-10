# Recipes/urls.py
from django.urls import path
from .views import home_view, RecipeListView, RecipeDetailView, records

app_name = 'recipes'  

urlpatterns = [
    path('', home_view, name='home'),
    path('recipes/', RecipeListView.as_view(), name='recipes-list'),  # Name matches here
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='detail'),
    path('records/', records, name='records'),
]

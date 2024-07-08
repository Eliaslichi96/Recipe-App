from django.urls import path
from .views import home_view, RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    path('', home_view, name='home'),
    path('recipes/', RecipeListView.as_view(), name='recipes-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='detail'),
]

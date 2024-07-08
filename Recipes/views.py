from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.
def home_view(request):
    return render(request, 'app/recipes_home.html')

class RecipeListView(ListView):
    model = Recipe
    template_name = "app/recipes_list.html"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "app/recipes_details.html"

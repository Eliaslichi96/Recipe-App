from django.test import TestCase
from .models import Recipe


# Create your tests here.
class RecipeModelTest(TestCase):
    def test_string_representation(self):
        recipe = Recipe(name="Pasta")
        self.assertEqual(str(recipe), recipe.name)

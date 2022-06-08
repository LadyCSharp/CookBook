from .models import Category, Recipes, Difficulty, Ingredients_group, Ingredient, MeasureUnit, Ingredient_Recipe
from .serializers import CategorySerializer, RecipeSerializer, DifficultySerializer, Ingredients_groupSerializer, \
    IngredientSerializer, MeasureUnitSerializer, Ingredient_RecipeSerializer
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer

class DifficultyViewSet(viewsets.ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer

class Ingredients_groupViewSet(viewsets.ModelViewSet):
    queryset = Ingredients_group.objects.all()
    serializer_class = Ingredients_groupSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class MeasureUnitViewSet(viewsets.ModelViewSet):
    queryset = MeasureUnit.objects.all()
    serializer_class = MeasureUnitSerializer

class Ingredient_RecipeViewSet(viewsets.ModelViewSet):
    queryset = Ingredient_Recipe.objects.all()
    serializer_class = Ingredient_RecipeSerializer
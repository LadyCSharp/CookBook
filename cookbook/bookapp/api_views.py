from .models import Category, Recipes, Difficulty, Ingredients_group, Ingredient, MeasureUnit, Ingredient_Recipe
from .serializers import CategorySerializer, RecipeSerializer, DifficultySerializer, Ingredients_groupSerializer, \
    IngredientSerializer, MeasureUnitSerializer, Ingredient_RecipeSerializer, Recipe1Serializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from .permissions import ReadOnly, IsAuthor

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.prefetch_related('ingredients')
    serializer_class = RecipeSerializer

class DifficultyViewSet(viewsets.ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer

class Ingredients_groupViewSet(viewsets.ModelViewSet):
    queryset = Ingredients_group.objects.all()
    serializer_class = Ingredients_groupSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class MeasureUnitViewSet(viewsets.ModelViewSet):
    queryset = MeasureUnit.objects.all()
    serializer_class = MeasureUnitSerializer

class Ingredient_RecipeViewSet(viewsets.ModelViewSet):
    queryset = Ingredient_Recipe.objects.all()
    serializer_class = Ingredient_RecipeSerializer

class Recipe1ViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.prefetch_related('ingredients')
    serializer_class = Recipe1Serializer
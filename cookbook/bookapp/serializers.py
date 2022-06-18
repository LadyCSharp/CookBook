# from django.conf.urls import url, include
from django.urls import path, include
from .models import Category, Recipes, Difficulty, Ingredients_group, Ingredient, MeasureUnit, Ingredient_Recipe
from rest_framework import routers, serializers, viewsets

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = serializers.StringRelatedField(many=True)
    class Meta:
        model = Recipes
        exclude = ['author']

class Recipe1Serializer(serializers.HyperlinkedModelSerializer):
    # Singredients = Recipes.display_sostav(self=self)
    sostav = serializers.StringRelatedField(source='display_sostav', read_only=True)
    ingredients = serializers.StringRelatedField(many=True)
    hi = serializers.BooleanField(source='has_image', read_only=True)
    picture = serializers.ImageField()
    class Meta:
        model = Recipes
        exclude = ['author']

class DifficultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Difficulty
        fields = '__all__'

class Ingredients_groupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredients_group
        fields = '__all__'

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class Ingredient_RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient_Recipe
        fields = '__all__'


class MeasureUnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MeasureUnit
        fields = '__all__'

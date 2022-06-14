from django import template
import os
import json
from bookapp.models import Recipes, Category, Ingredients_group, Ingredient_Recipe
register = template.Library()


def open(path):
    rez = []
    if os.path.exists(path) == False:
        return rez
    with open(path, 'r') as f:
        rez = json.load(f)


    return rez









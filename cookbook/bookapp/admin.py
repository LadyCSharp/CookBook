from django.contrib import admin
from bookapp.models import Category, Ingredients_group, Ingredient, Difficulty, Recipes

# Register your models here.
admin.site.register(Category)
admin.site.register(Ingredients_group)
admin.site.register(Ingredient)
admin.site.register(Difficulty)
admin.site.register(Recipes)
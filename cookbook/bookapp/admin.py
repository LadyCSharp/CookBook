from django.contrib import admin
from bookapp.models import Category, Ingredients_group, Ingredient, Difficulty, Recipes, MeasureUnit, Ingredient_Recipe
from django.db.models import F
from operator import xor

# Register your models here.
admin.site.register(Category)
admin.site.register(Ingredients_group)
admin.site.register(Ingredient)
admin.site.register(Difficulty)

def clear_rating(modeladmin, request, queryset):
    queryset.update(portions=2)


clear_rating.short_description = "Выставить количество порций = 2"

def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

def inverse_active(modeladmin, request, queryset):
    queryset.update(is_active=(bool(F('is_active')) != True))


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'text','display_sostav', 'category' ,'difficulty', 'has_image', 'portions', 'is_active']
    actions = [clear_rating, set_active, inverse_active]


admin.site.register(Recipes, PostAdmin)
admin.site.register(MeasureUnit)
admin.site.register(Ingredient_Recipe)
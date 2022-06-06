from django.core.management.base import BaseCommand
from bookapp.models import Category, Ingredient, Ingredients_group, Difficulty, Recipes

class Command(BaseCommand):

    def handle(self, *args, **options):
        veget = ['Огурец', 'Помидор', 'Лук репчатый', 'Соль', 'Сметана']

        # # Создание
        # for ovosch in veget:
        # Ingredient.objects.create(name='Сметана', group=Ingredients_group.objects.get(name='Молоко/масло'))
        # rec_text = 'Помидоры, огурцы и лук нарезать крупными кусками, посолить, заправить сметаной'
        #
        # Recipes.objects.create(name='Салат со сметаной', \
        #                        category= Category.objects.get(name = 'Закуски'), \
        #                        difficulty = Difficulty.objects.get(name = 'Средне'),\
        #                        duration = '00:15', portions = 2, text=rec_text)
        R = Recipes.objects.get(name='Салат со сметаной')
        for ovosch in veget:
            R.ingredients.add( Ingredient.objects.get(name=ovosch))


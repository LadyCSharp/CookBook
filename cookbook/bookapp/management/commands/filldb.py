from django.core.management.base import BaseCommand
from bookapp.models import Category, Ingredient, Ingredients_group, Difficulty, Recipes
import os.path
from pathlib import Path
import json
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
def jopen(path):
    rez = []

    if os.path.exists(path) == False:

        print("файл не найден")
        print(path)
        return rez
    with open(path, 'r') as f:
        rez = json.load(f)


    return rez

class Command(BaseCommand):

    def handle(self, *args, **options):
        path = os.path.join(BASE_DIR, 'data', 'result.json')
        rez = jopen(path)
        rez = rez["messages"]
        for item in rez:
            print(item)
            if item['text']:
                recipe = Recipes.create(item['text'][:10])

        # veget = ['Огурец', 'Помидор', 'Лук репчатый', 'Соль', 'Сметана']
        #
        # # # Создание
        # # for ovosch in veget:
        # # Ingredient.objects.create(name='Сметана', group=Ingredients_group.objects.get(name='Молоко/масло'))
        # # rec_text = 'Помидоры, огурцы и лук нарезать крупными кусками, посолить, заправить сметаной'
        # #
        # # Recipes.objects.create(name='Салат со сметаной', \
        # #                        category= Category.objects.get(name = 'Закуски'), \
        # #                        difficulty = Difficulty.objects.get(name = 'Средне'),\
        # #                        duration = '00:15', portions = 2, text=rec_text)
        # R = Recipes.objects.get(name='Салат со сметаной')
        # for ovosch in veget:
        #     R.ingredients.add( Ingredient.objects.get(name=ovosch))



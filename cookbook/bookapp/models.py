from django.db import models
from userapp.models import BookUser
# Create your models here.
class TimeStamp(models.Model):
    """
    Abstract - для нее не создаются новые таблицы
    данные хранятся в каждом наследнике
    """
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Mother(models.Model):
    """
    Abstract - для нее не создаются новые таблицы
    данные хранятся в каждом наследнике
    """
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True
class Category(TimeStamp, Mother):
    # Id не надо, он уже сам появится


    def __str__(self):
        return self.name

class Difficulty(Mother):




    def __str__(self):
        return self.name

class Ingredients_group(Mother):




    def __str__(self):
        return self.name

class Ingredient(Mother):

    group = models.ForeignKey(Ingredients_group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Recipes(TimeStamp, Mother):

    picture = models.ImageField(upload_to='posts', null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, through='Ingredient_Recipe')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    duration = models.TimeField()
    portions = models.PositiveSmallIntegerField()
    text = models.TextField()
    author = models.ForeignKey(BookUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, category: {self.category.name}'

    def has_image(self):
        # print('my image:', self.image)
        # print('type', type(self.image))
        return bool(self.picture)


class MeasureUnit(Mother):
    def __str__(self):
        return self.name


class Ingredient_Recipe(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, db_index=False)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, db_index=False)
    count = models.PositiveSmallIntegerField()
    measureunit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            'recipe',
            'ingredient',
        )
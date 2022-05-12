from django.db import models

# Create your models here.

class Category(models.Model):
    # Id не надо, он уже сам появится
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Difficulty(models.Model):

    name = models.CharField(max_length=16, unique=True)


    def __str__(self):
        return self.name

class Ingredients_group(models.Model):

    name = models.CharField(max_length=16, unique=True)


    def __str__(self):
        return self.name

class Ingredient(models.Model):

    name = models.CharField(max_length=16, unique=True)
    group = models.ForeignKey(Ingredients_group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Recipes(models.Model):
    name = models.CharField(max_length=16, unique=True)
    picture = models.ImageField()
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    duration = models.TimeField()
    portions = models.PositiveSmallIntegerField()
    text = models.TextField()
    def __str__(self):
        return self.name
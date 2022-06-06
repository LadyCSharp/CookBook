from django.db import models
from userapp.models import BookUser
from django.utils.functional import cached_property

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
class ActiveManager(models.Manager):

    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)


class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    is_active = models.BooleanField(default=False)

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

class Recipes(TimeStamp, Mother, IsActiveMixin):

    picture = models.ImageField(upload_to='posts', null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, through='Ingredient_Recipe', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_recipe')
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

    # @cached_property
    # def display_sostav(self):
    #     result = list()
    #     ingredients = self.ingredients.all()
    #     for item in ingredients:
    #         r = Ingredient_Recipe.objects.get(recipe=self, ingredient=item).str1
    #         #result += item.name + ' ' +r +'<br>'
    #         result.append(item.name + ' ' +r )
    #     return result
    # @cached_property
    # def display_sostav(self):
    #
    #     items = Ingredient_Recipe.objects.filter(recipe=self).all()
    #     result = ' '.join([item.str1() for item in items])
    #     print(result)
    #     return result
    def display_sostav(self):
        result = list()
        ingredients = self.ingredients.all()
        for item in ingredients:
            r = Ingredient_Recipe.objects.get(recipe=self, ingredient=item).str1()
            # result += item.name + ' ' +r +'<br>'
            result.append(item.name + ' ' + r)
        return result
    @classmethod
    def create(cls, name):
        recipe = cls(name=name)
        # do something with the book
        return recipe

class MeasureUnit(Mother):
    def __str__(self):
        return self.name


class Ingredient_Recipe(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, db_index=False)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, db_index=False, related_name='sostav')
    value = models.PositiveSmallIntegerField()
    measureunit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            'recipe',
            'ingredient',
        )

    #S   @cached_property
    def str1(self):
        return f'{self.ingredient} {str(self.value)}  {self.measureunit.name}'

    # def __str__(self):
    #     return f'{self.recipe} {self.ingredient} {str(self.value)}  {self.measureunit.name}'
    #    @cached_property
    def __str__(self):
        return f'{self.ingredient} {str(self.value)} {self.measureunit.name}'



# class RecipeManager(models.Manager):
#     def create_recipe(self, name, text):
#         recipe = self.create(nane=name, text=text)
#         # do something
#         return recipe
# models.CASCADE: автоматически удаляет строку из зависимой таблицы, если удаляется связанная строка из главной таблицы
#
# models.PROTECT: блокирует удаление строки из главной таблицы, если с ней связаны какие-либо строки из зависимой таблицы
#
# models.SET_NULL: устанавливает NULL при удалении связанной строка из главной таблицы
#
# models.SET_DEFAULT: устанавливает значение по умолчанию для внешнео ключа в зависимой таблице. В этом случае для этого столбца должно быть задано значение по умолчанию
#
# models.DO_NOTHING: при удалении связанной строки из главной таблицы не производится никаких действий в зависимой таблице
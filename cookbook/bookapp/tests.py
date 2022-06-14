from django.test import TestCase
# faker - простые данные, например случайное имя
from faker import Faker
# FactoryBoy - данные для конкретной модели django
# mixer - полностью создать fake модель
from mixer.backend.django import mixer
# Create your tests here.


from .models import Recipes, Category, Difficulty
from userapp.models import BookUser

class RecipeTestCase(TestCase):

    def setUp(self):
        category = Category.objects.create(name='test_category')
        difi = Difficulty.objects.create(name='test_dif')
        user = BookUser.objects.create_user(username='test_user', email='test@test.com', password='mary1234567')
        self.post = Recipes.objects.create(name='test_post', text='some', author=user, category=category,
                                           duration="00:10:00", portions=1, difficulty=difi)

        self.post_str = Recipes.objects.create(name='test_post_str', text='some', author=user, category=category,
                                               duration="00:10:00", portions=1, difficulty=difi)

    def test_has_image(self):
        self.assertFalse(self.post.has_image())


    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str, category: test_category')


class RecipeTestCaseFaker(TestCase):

    def setUp(self):
        faker = Faker()
        category = Category.objects.create(name=faker.name())
        difi = Difficulty.objects.create(name=faker.name())
        user = BookUser.objects.create_user(username=faker.name(), email='test@test.com', password='1234567')
        self.post = Recipes.objects.create(name=faker.name(), text=faker.name(), author=user, category=category,
                                           duration=faker.time(), portions=faker.random_int(10), difficulty=difi)

        print(self.post.name)
        print(category.name)

        category = Category.objects.create(name='test_category')
        self.post_str = Recipes.objects.create(name='test_post_str', text='some', author=user, category=category,
                                               duration=faker.time(), portions=faker.random_int(10), difficulty=difi)

    def test_has_image(self):
        self.assertFalse(self.post.has_image())



    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str, category: test_category')


class PostTestCaseMixer(TestCase):

    def setUp(self):
        self.post = mixer.blend(Recipes)

        # print('mixer-name:', self.post.name)
        # print('mixer-category', self.post.category)
        # print('mixer-category-type', type(self.post.category))
        # print('mixer-user-email', self.post.user.email)
        # Как создать картинку с mixer?

        # Хороший вариант
        # category = mixer.blend(Category, name='test_category')
        # self.post_str = mixer.blend(Post, name='test_post_str', category=category)

        # Короткая запись
        self.post_str = mixer.blend(Recipes, name='test_post_str', category__name='test_category')

    def test_has_image(self):
        self.assertFalse(self.post.has_image())



    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str, category: test_category')
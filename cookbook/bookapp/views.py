from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Ingredient
from .models import Recipes, Category, Ingredients_group, Ingredient_Recipe
from .forms import ContactForm, PostForm, RecipeCategoryForm, SostavForm
from django.core.mail import send_mail
from django.views.generic.base import ContextMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django import forms
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
# def main_view(request):
#     posts = Recipes.objects.all()
#     return render(request, 'bookapp/index.html', context={'posts': posts})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получить данные из формы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            send_mail(
                'Contact message',
                f'Ваш сообщение {message} принято',
                'from@example.com',
                [email],
                fail_silently=True,
            )

            return HttpResponseRedirect(reverse('cookbook:index'))
        else:
            return render(request, 'bookapp/contact.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'bookapp/contact.html', context={'form': form})

def post(request, id):
    post = get_object_or_404(Recipes, id=id)
    return render(request, 'bookapp/post.html', context={'post': post})

@login_required
def create_recipe(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'bookapp/create.html', context={'form': form})
    else:
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return HttpResponseRedirect(reverse('cookbook:index'))
        else:
            return render(request, 'bookapp/create.html', context={'form': form})

class NameContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Продукты:'
        return context
# CRUD CREATE, READ (LIST, DETAIL), UPDATE, DELETE
# список тегов
class IngredientListView(ListView, NameContextMixin):
    model = Ingredient
    template_name = 'bookapp/ingredient_list.html'
    paginate_by = 20
    context_object_name = 'Ingredient'



class IngredientFilterListView(ListView, NameContextMixin):
    model = Ingredient
    template_name = 'bookapp/ingredient_list.html'
    context_object_name = 'Ingredient'

    def get_queryset(self):

        self.group = get_object_or_404(Ingredients_group, id=self.kwargs['pk'])
        return Ingredient.objects.filter(group=self.group)




# детальная информация
class IngredientDetailView(DetailView, NameContextMixin):
    fields = '__all__'
    model = Ingredient
    template_name = 'bookapp/ingredient_detail.html'

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.tag_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Получение этого объекта
        :param queryset:
        :return:
        """
        return get_object_or_404(Ingredient, pk=self.tag_id)


# создание тега
class IngredientCreateView(LoginRequiredMixin, CreateView, NameContextMixin):
    # form_class =
    fields = '__all__'
    model = Ingredient
    success_url = reverse_lazy('cookbook:ingredient_list')
    template_name = 'bookapp/ingredient_create.html'

    def post(self, request, *args, **kwargs):
        """
        Пришел пост запрос
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Метод срабатывает после того как форма валидна
        :param form:
        :return:
        """
        return super().form_valid(form)


class IngredientUpdateView(LoginRequiredMixin,UpdateView):
    fields = '__all__'
    model = Ingredient
    success_url = reverse_lazy('cookbook:ingredient_list')
    template_name = 'bookapp/ingredient_create.html'


class IngredientDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'bookapp/ingredient_delete.html'
    model = Ingredient
    success_url = reverse_lazy('cookbook:ingredient_list')

class GroupListView(ListView, NameContextMixin):
    model = Ingredients_group
    template_name = 'bookapp/ingredient_group.html'
    context_object_name = 'Group'

    # def get_queryset(self):
    #     """
    #     Получение данных
    #     :return:
    #     """
    #     return Ingredient.objects.filter()


class MainView(ListView):
    model = Recipes
    title = 'вкуСняшки от Машки'
    template_name = 'bookapp/main.html'
    paginate_by = 10
    context_object_name = 'Recipes'

    # class Meta:
    #     ordering = ['-id']


    def get_queryset(self):
        return Recipes.active_objects.order_by('name').all()



class RecipeCreateView(LoginRequiredMixin, CreateView):
    # form_class =
    model = Recipes
    # fields = '__all__'
    # exclude = ('author')
    form_class = PostForm

    template_name = 'bookapp/recipe_create.html'
    def form_valid(self, form):
        """
        Метод срабатывает после того как форма валидна
        :param form:
        :return:
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('bookapp:sostav_create')

class RecipeDetailView(DetailView):
    fields = '__all__'

    model = Recipes
    # ingredient = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(),
    #                                       widget=forms.CheckboxSelectMultiple())
    template_name = 'bookapp/recipe_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(RecipeDetailView, self).get_context_data(**kwargs)
    #     context['sostav'] = Ingredient_Recipe.objects.filter(
    #         recipe=self.object)
    #     print(context)
    #     return context

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.tag_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Получение этого объекта
        :param queryset:
        :return:
        """
        return get_object_or_404(Recipes, pk=self.tag_id)

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    fields = '__all__'
    exclude = ('ingredient')
    model = Recipes

    template_name = 'bookapp/recipe_create.html'
    def form_valid(self, form):
        """
        Метод срабатывает после того как форма валидна
        :param form:
        :return:
        """
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Получение этого объекта
        :param queryset:
        :return:
        """

        return get_object_or_404(Recipes, pk=self.id)

    def get_success_url(self):
        return reverse('bookapp:sostav_update', kwargs={'pk': self.id})

class RecipeDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'bookapp/ingredient_delete.html'
    model = Recipes
    success_url = reverse_lazy('cookbook:index')

    def test_func(self):
        return self.request.user.is_superuser


class CategoryDetailView(DetailView):
    template_name = 'bookapp/category_detail.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeCategoryForm()
        return context

class CategoryListView(ListView):
    model = Category
    template_name = 'bookapp/category_list.html'
    paginate_by = 10 #20


class RecipeCategoryCreateView(CreateView):
    model = Recipes
    template_name = 'bookapp/category_detail.html'
    success_url = reverse_lazy('')
    form_class = RecipeCategoryForm

    def post(self, request, *args, **kwargs):
        self.category_pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        category = get_object_or_404(Category, pk=self.category_pk)
        form.instance.category = category
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('bookapp:category_detail', kwargs={'pk': self.category_pk})


class SostavCreateView(CreateView):
    model = Ingredient_Recipe
    template_name = 'bookapp/sostav_create.html'
    success_url = reverse_lazy('')
    form_class = SostavForm

    def post(self, request, *args, **kwargs):
        self.recipe_pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):

        recipe = get_object_or_404(Recipes, pk=self.pk)
        form.instance.recipe = recipe
        return super().form_valid(form)

    def get_success_url(self):

        return reverse('bookapp:recipe_detail', kwargs={'pk': self.recipe.pk})


class SostavUpdateView(UpdateView):
    model = Ingredient_Recipe
    template_name = 'bookapp/sostav_create.html'
    success_url = reverse_lazy('')
    form_class = SostavForm

    def post(self, request, *args, **kwargs):
        self.recipe_pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        recipe = get_object_or_404(Recipes, pk=self.pk)
        form.instance.recipe = recipe
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('bookapp:recipe_detail', kwargs={'pk': self.recipe.pk})



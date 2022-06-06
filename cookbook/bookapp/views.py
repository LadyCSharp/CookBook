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
from django.forms import formset_factory, modelformset_factory, inlineformset_factory

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
    # fields = ('picture',
    #           'category',
    #           'difficulty',
    #           'duration',
    #           'portions',
    #           'text')
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
        #return reverse('bookapp:sostav_update')
        return reverse('bookapp:sostav_recipe', kwargs={'id': self.object.id} )



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
    fields = ('name',
        'picture',
    'category' ,
    'difficulty',
    'duration',
    'portions',
    'text')

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

    def post(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.r_id = kwargs['pk']
        return super().get(request, *args, **kwargs)



    def get_success_url(self):
        #return reverse('bookapp:sostav_update', kwargs={'pk': self.id})
        return reverse('bookapp:sostav_recipe', kwargs={'id': self.pk})

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


# class SostavCreateView(CreateView):
#     model = Ingredient_Recipe
#     template_name = 'bookapp/sostav_create.html'
#     success_url = reverse_lazy('')
#     #form_class = SostavForm
#     SostavFormSet = formset_factory(SostavForm, extra=1)
#
#     def post(self, request, *args, **kwargs):
#         self.recipe_pk = kwargs['pk']
#         return super().post(request, *args, **kwargs)
#
#     def form_valid(self, form):
#
#         recipe = get_object_or_404(Recipes, pk=self.pk)
#         form.instance.recipe = recipe
#         return super().form_valid(form)
#
#     def get_success_url(self):
#
#         return reverse('bookapp:recipe_detail', kwargs={'pk': self.recipe.pk})


class SostavUpdateView(UpdateView):
    model = Ingredient_Recipe
    fields = '__all__'
    template_name = 'bookapp/sostav_create.html'
    success_url = reverse_lazy('')
    SostavFormSet = formset_factory(SostavForm, extra=1)

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

        def get_queryset(self):
            self.recipe = get_object_or_404(Recipes, id=self.kwargs['pk'])
            return Ingredient_Recipe.objects.filter(recipe=self.recipe)


    def form_valid(self, form):
        recipe = get_object_or_404(Recipes, pk=self.pk)
        form.instance.recipe = recipe
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('bookapp:recipe_detail', kwargs={'pk': self.recipe.pk})



def managesostav(request, id):
    recipe = get_object_or_404(Recipes, id=id)
    SostavFormSet = modelformset_factory(Ingredient_Recipe, fields = '__all__')
    if request.method == 'POST':
        formset = SostavFormSet(request.POST, request.FILES, queryset=Ingredient_Recipe.objects.filter(recipe=recipe))
        if formset.is_valid():

            formset.save()
            # do something.
            return HttpResponseRedirect(reverse('bookapp:recipe_detail', kwargs={'pk': id}))
    else:
        formset = SostavFormSet(queryset=Ingredient_Recipe.objects.filter(recipe=recipe))
    return render(request, 'bookapp/sostav_create.html', {'formset': formset})



def SostavRecipe(request, id):
    recipe = get_object_or_404(Recipes, id=id)
    SostavFormSet = modelformset_factory(Ingredient_Recipe, fields = '__all__', extra=1) #, exclude=('recipe',)
    RecipeForm = modelformset_factory(Recipes, fields = '__all__',extra=0)  #, exclude=('is_active',)
    if request.method == 'POST':
        sostav_formset = SostavFormSet(request.POST, request.FILES, prefix='sostav', queryset=Ingredient_Recipe.objects.filter(recipe=recipe))
        recipe_formset = RecipeForm(request.POST, request.FILES, prefix='recipe',queryset=Recipes.objects.filter(id=id))
        if sostav_formset.is_valid() and recipe_formset.is_valid():
            # do something with the cleaned_data on the formsets.
            #recipe_formset.save()
            sf=sostav_formset.save(commit=False)
            for f in sf:
                #f.instance.recipe = recipe
                f.save()

            sostav_formset.save_m2m()
            recipe_formset.save_m2m()
            recipe_formset.save()
            return HttpResponseRedirect(reverse('bookapp:recipe_detail', kwargs={'pk': id}))
    else:
        sostav_formset = SostavFormSet(prefix='articles', queryset=Ingredient_Recipe.objects.filter(recipe=recipe))
        recipe_formset = RecipeForm(prefix='books',queryset=Recipes.objects.filter(id=id))
    return render(request, 'bookapp/sostav_recipe.html', {
        'sostav_formset': sostav_formset,
        'recipe_formset': recipe_formset,
    })


def alsorecipe(request, id):
    recipe = get_object_or_404(Recipes, id=id)
    SostavFormSet = inlineformset_factory(Recipes, Ingredient_Recipe, fields='__all__',extra=1)
    if request.method == "POST":
        formset = SostavFormSet(request.POST, request.FILES,instance=recipe)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(reverse('bookapp:recipe_detail', kwargs={'pk': id}))
    else:
        formset = SostavFormSet(instance=recipe)
    return render(request, 'bookapp/sostav_create.html', {'formset': formset})


class RecipeUpdatePlusView(LoginRequiredMixin, UpdateView):
    fields = ('picture',
    'category' ,
    'difficulty',
    'duration',
    'portions',
    'text')

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

    def post(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.r_id = kwargs['pk']
        return super().get(request, *args, **kwargs)



    def get_success_url(self):
        #return reverse('bookapp:sostav_update', kwargs={'pk': self.id})
        return reverse('bookapp:manage_sostav', kwargs={'id': self.pk})

from django import forms
from .models import Recipes
from .models import Ingredient, Ingredient_Recipe
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



class ContactForm(forms.Form):
    name = forms.CharField(label='Название')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')


class PostForm(forms.ModelForm):
    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={'placeholder': 'Название', 'class': 'form-control'}))
    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(attrs={'placeholder': 'Описание', 'class': 'form-control'}))
    duration = forms.DurationField(label='Время приготовления',widget=forms.TextInput(attrs={'placeholder': 'Название', 'class': 'form-control'}))
    portions = forms.CharField(label="Количество порций", widget=forms.NumberInput())
    text = forms.CharField(label='Технология приготовления',
                                  widget=forms.Textarea(attrs={'placeholder': 'Технология приготовления', 'class': 'form-control'}))
    # picture = models.ImageField(upload_to='posts', null=True, blank=True)
    # ingredients = models.ManyToManyField(Ingredient, through='Ingredient_Recipe', blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_recipe', db_index=True)
    # difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    # duration = models.TimeField()
    # portions = models.PositiveSmallIntegerField()
    # text = models.TextField()
    # # Чекбоксы
    # ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(),
    #                                       widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Recipes
        # fields = '__all__'
        # fields = ('name', 'category')
        exclude = ('ingredients', 'author', 'is_active')



class RecipeCategoryForm(forms.ModelForm):
    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))

    # # Чекбоксы
    # ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(),
    #                                       widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Recipes
        # fields = '__all__'
        # fields = ('name', 'category')
        exclude = ('category', 'ingredients', 'author', 'is_active')


class SostavUpdateForm(forms.ModelForm):
    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))



    class Meta:
        model = Ingredient_Recipe
        # fields = '__all__'
        # fields = ('name', 'category')
        exclude = ('recipe',)

class RecipeUpdateForm(forms.ModelForm):
    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    description = forms.CharField(label='Описание',
                                  widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))

    # picture = models.ImageField(upload_to='posts', null=True, blank=True)
    # ingredients = models.ManyToManyField(Ingredient, through='Ingredient_Recipe', blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_recipe', db_index=True)
    # difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    # duration = models.TimeField()
    # portions = models.PositiveSmallIntegerField()
    # text = models.TextField()
    # # Чекбоксы
    # ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(),
    #                                       widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Recipes
        # fields = '__all__'
        # fields = ('name', 'category')
        exclude = ('ingredients', 'author', 'is_active')

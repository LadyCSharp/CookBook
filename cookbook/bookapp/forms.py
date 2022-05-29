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
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))

    # # Чекбоксы
    # ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(),
    #                                       widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Recipes
        # fields = '__all__'
        # fields = ('name', 'category')
        exclude = ('ingredients', 'author')


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
        exclude = ('category', 'ingredients', 'author')


class SostavForm(forms.ModelForm):
    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))



    class Meta:
        model = Ingredient_Recipe
        # fields = '__all__'
        # fields = ('name', 'category')
        exclude = ('recipe',)



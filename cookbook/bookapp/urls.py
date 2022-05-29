from django.urls import path
from bookapp import views


app_name = 'bookapp'

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('create/', views.RecipeCreateView.as_view(), name='create'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:id>/', views.post, name='post'),
    path('recipe-detail/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('ingredient-list', views.IngredientListView.as_view(), name='ingredient_list'),
    path('ingredient-detail/<int:pk>/', views.IngredientDetailView.as_view(), name='ingredient_detail'),
    path('ingredient-create/', views.IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredient-update/<int:pk>/', views.IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredient-delete/<int:pk>/', views.IngredientDeleteView.as_view(), name='ingredient_delete'),
    path('ingredient-list/<int:pk>/', views.IngredientFilterListView.as_view(), name='ingredient_list'),
    path('ingredient-group', views.GroupListView.as_view(), name='ingredient_group'),
    path('recipe-update/<int:pk>/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe-delete/<int:pk>/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    path('category-detail/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category-list', views.CategoryListView.as_view(), name='category_list'),
    path('category-create/<int:pk>/', views.RecipeCategoryCreateView.as_view(), name='recipe_category_create'),
    path('category-update/<int:pk>/', views.RecipeCategoryCreateView.as_view(), name='category_update'),
    path('sostav-create', views.SostavCreateView.as_view(), name='sostav_create'),
    path('sostav-update/<int:pk>/', views.SostavUpdateView.as_view(), name='sostav_update'),
]


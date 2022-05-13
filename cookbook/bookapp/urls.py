from django.urls import path
from bookapp import views


app_name = 'bookapp'
#app_name = 'cookbook'
urlpatterns = [
    path('', views.main_view, name='index'),
    path('create/', views.create_recipe, name='create'),
    path('post/<int:id>/', views.post, name='post'),
]


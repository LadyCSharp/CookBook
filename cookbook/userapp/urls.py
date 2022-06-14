from django.urls import path
from userapp import views
from django.contrib.auth.views import LogoutView

app_name = 'userapp'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('profile-list', views.ProfileListView.as_view(), name='profile_list'),
    path('profile-detail/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile-create/', views.ProfileCreateView.as_view(), name='profile_create'),
    path('profile-update/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile-delete/<int:pk>/', views.ProfileDeleteView.as_view(), name='profile_delete'),
    path('update-token/', views.update_token, name='update_token'),
    path('update-token-ajax/', views.update_token_ajax),
]


"""cookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from bookapp.api_views import CategoryViewSet, RecipeViewSet, DifficultyViewSet, Ingredients_groupViewSet, \
    IngredientViewSet, MeasureUnitViewSet, Ingredient_RecipeViewSet, Recipe1ViewSet
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'recipe1', Recipe1ViewSet)
router.register(r'difficulty', DifficultyViewSet)
router.register(r'ingredients_group', Ingredients_groupViewSet)
router.register(r'ingredient', IngredientViewSet)
router.register(r'measureunit', MeasureUnitViewSet)
router.register(r'ingredientrecipe', Ingredient_RecipeViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookapp.urls', namespace='cookbook')),
    path('users/', include('userapp.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/v0/categories/', include(router.urls)),
    # path('api/v0/posts/', include(router_p.urls)),
    path('api/v0/', include(router.urls)),
]



if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),


    ] + urlpatterns
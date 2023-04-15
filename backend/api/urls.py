from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (IngredientViewSet, RecipeViewSet, TagViewSet,
                       CustomUserViewSet)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('ingredients', IngredientViewSet)
router_v1.register('recipes', RecipeViewSet)
router_v1.register('tags', TagViewSet)
router_v1.register('users', CustomUserViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]

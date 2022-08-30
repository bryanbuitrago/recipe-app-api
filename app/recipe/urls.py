""" 
URL mappings for the recipe app.
"""

from importlib.resources import path
from xml.etree.ElementInclude import include
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]

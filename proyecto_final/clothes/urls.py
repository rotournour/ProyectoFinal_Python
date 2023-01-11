from django.urls import path, include

from clothes.views import create_clothing, list_categories, list_clothes


urlpatterns = [
    path('vender/', create_clothing),
    path('listado_categories/', list_categories),
    path('listado_clothes/', list_clothes),]
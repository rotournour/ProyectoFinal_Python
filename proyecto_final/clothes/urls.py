from django.urls import path, include

from clothes.views import create_clothing, list_categories, list_clothes, clothes_update

urlpatterns = [
    path('vender/', create_clothing),
    path('listado_categories/', list_categories),
    path('listado_clothes/', list_clothes),
    path('update-clothes/<int:pk>/', clothes_update)
    
    ]
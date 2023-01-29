from django.urls import path

from clothes.views import create_clothing, list_categories, list_and_buy, clothes_update, ClothesDeleteView

urlpatterns = [
    path('create/', create_clothing),
    path('listado_categories/', list_categories), #arreglar
    path('listado_clothes/', list_and_buy), #arreglar
    path('update-clothes/<int:pk>/', clothes_update),
    path('delete-clothes/<int:pk>/', ClothesDeleteView.as_view(), name= 'delete_clothes'),
    
    ]
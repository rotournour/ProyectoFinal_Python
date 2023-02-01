from django.urls import path

from clothes.views import create_clothing, list_categories, list_and_buy, clothes_update, ClothesDeleteView

urlpatterns = [
    path('create/', create_clothing),
    path('list-categories/', list_categories), 
    path('list-clothes/', list_and_buy), 
    path('update-clothes/<int:pk>/', clothes_update),
    path('delete-clothes/<int:pk>/', ClothesDeleteView.as_view(), name= 'delete_clothes'),
    
    ]
from django.urls import path, include

from sales.views import create_order


urlpatterns = [
    path('order/', create_order),]
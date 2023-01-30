from django.contrib import admin
from django.urls import path, include
from proyecto_final.views import index
from proyecto_final.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('clothes/', include('clothes.urls')),
    path('users/', include('users.urls'))] + static(MEDIA_URL, document_root = MEDIA_ROOT)
from django.urls import path
from users.views import user_login
from django.contrib.auth.views import LogoutView
from users.views import register


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    path('signup/', register, name = 'register'),]

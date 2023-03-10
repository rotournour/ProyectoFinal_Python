from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import register, update_user, update_profile, user_login, UserListView


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    path('signup/', register, name = 'register'),
    path('update-user/', update_user),
    path('update-profile/', update_profile),
    path('my-profile/', UserListView.as_view(template_name='users/my-profile.html') )
    
    ]


from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label='Nombre de usuario')
    class Meta:
        model = User
        fields = ['username']
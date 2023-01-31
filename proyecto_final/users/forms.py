from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from users.models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = { 'username': ('Nombre de usuario' ), 'first_name': ('Nombre:'), 'last_name' :('Apellido:')}
        
        
        

class UpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label='Nombre de usuario')
    class Meta:
        model = User
        fields = ['username']
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone', 'birth_date', 'profile_picture']
        labels = { 'first_name': 'Nombre ', 'last_name': 'Apellido:', 'phone': ('Número de telefono:' ), 'birth_date': ('Cual es tu fecha de nacimiento?:'), 'profile_picture' :('Foto de perfil:') }
        

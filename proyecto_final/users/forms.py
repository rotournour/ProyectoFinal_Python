from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from users.models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        

class UpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label='Nombre de usuario')
    class Meta:
        model = User
        fields = ['username']
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'birth_date', 'profile_picture']
        labels = { 'phone': ('Número de telefono:' ), 'birth_date': ('Cual es tu fecha de nacimiento?:'), 'profile_picture' :('Foto de perfil:') }
        

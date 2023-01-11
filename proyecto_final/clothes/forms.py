from django import forms
from clothes.models import Gender, Type_Clothing

class ClothingForm(forms.Form):
    name = forms.CharField(max_length=100, label= 'Nombre de la prenda')
    price = forms.FloatField(label= 'Precio')
    category = forms.ModelChoiceField(queryset= Type_Clothing.objects.all(), label= 'Categoria de la prenda')
    brand = forms.CharField(max_length= 50, label= 'Marca de la prenda')
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(), label= 'Para quien es la prenda?')
    new_clothing = forms.BooleanField(label= 'Tu prenda es nueva?')
    stock = forms.BooleanField(required=False)
    
from django import forms
from clothes.models import Gender, Type_Clothing, Clothes
from sales.models import Payment

class ClothForm(forms.Form):
    name = forms.CharField(max_length=100, label= 'Nombre de la prenda')
    price = forms.FloatField(label= 'Precio')
    category = forms.ModelChoiceField(queryset= Type_Clothing.objects.all(), label= 'Categoria de la prenda')
    brand = forms.CharField(max_length= 50, label= 'Marca de la prenda')
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(), label= 'Para quien es la prenda?')
    new_clothing = forms.BooleanField(label= 'Tu prenda es nueva?', required=False)
    
    
class UpdateCloth (forms.ModelForm):
    class Meta: 
        model = Clothes
        fields = ['price']
    
class ClothesCart(forms.Form):
    buyer = forms.CharField(max_length=100, label= 'Tu username: ')
    cloth = forms.IntegerField(widget= forms.HiddenInput, initial = 1)
    type_payment = forms.ModelChoiceField(queryset=Payment.objects.all(), label = 'Medio de pago: ')
from django import forms
from clothes.models import Type_Clothing
from sales.models import Payment

class SalesForm(forms.Form):
    client = forms.CharField(max_length=123, label = 'Cliente')
    clothes_name = forms.CharField(max_length=123, label = 'Prenda')
    category = forms.ModelChoiceField(queryset=Type_Clothing.objects.all(), label= 'Categoria de la prenda')
    payment = forms.ModelChoiceField(queryset=Payment.objects.all(), label= 'Metodo de pago')
    
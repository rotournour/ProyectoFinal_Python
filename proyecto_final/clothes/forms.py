from django import forms
from clothes.models import Gender, Type_Clothing, Clothes
from sales.models import Payment

    
class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['name', 'seller_username', 'price', 'category', 'size', 'brand', 'gender', 'new_clothing', 'cloth_picture']
        labels = { 'name': ('Nombre de la prenda:' ), 'seller_username': ('Usuario del vendedor'), 'price' : ('Precio:'), 'category' : ('Categoria de la prenda:'), 'size': ('Talle de la prenda'),  'brand' : ('Marca de la prenda:'), 'gender' : ('Para quien es la prenda?'), 'new_clothing' : ('La prenda es nueva?'), 'cloth_picture' : ('Sube una foto:') }
    
    
    
class UpdateCloth (forms.ModelForm):
    class Meta: 
        model = Clothes
        fields = ['price']
    
class ClothesCart(forms.Form):
    buyer = forms.CharField(max_length=100, label= 'Tu username: ')
    cloth = forms.IntegerField(widget= forms.HiddenInput, initial = 1)
    type_payment = forms.ModelChoiceField(queryset=Payment.objects.all(), label = 'Medio de pago: ')
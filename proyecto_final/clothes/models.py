from django.db import models
from sales.models import Payment


class Gender (models.Model):
    genders = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.genders
    
    class Meta():
        db_table = "Genders"
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

class Type_Clothing (models.Model):
    categories= models.CharField(max_length=30)
    
    class Meta():
        db_table = "Type_of_clothing"
        verbose_name = 'Type of clothes'
        verbose_name_plural = 'Type of clothes'
        
    def __str__(self):
        return self.categories

class Clothes (models.Model):
    name = models.CharField(max_length=100, verbose_name= "Nombre de la prenda")
    price = models.FloatField(verbose_name= "Precio de la prenda")
    category = models.ForeignKey(Type_Clothing, null=True, blank=True, on_delete=models.CASCADE, verbose_name= "Tipo de prenda")
    gender = models.ForeignKey(Gender, null=True, blank=True, on_delete=models.CASCADE, verbose_name= "Genero de la prenda")
    brand = models.CharField(max_length=50, null=True, verbose_name= "Marca de la prenda")
    new_clothing = models.BooleanField (verbose_name= "Prenda nueva")
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.CASCADE, verbose_name= "Medio de pago" )
    is_available = models.BooleanField(default=True)

    
    class Meta():
        db_table = "Clothes"
        verbose_name = 'Clothes'
        verbose_name_plural = 'Clothes'

    def __str__(self):
        return f'{self.name} de marca {self.brand} con un precio de {self.price}'
    
    def setUnavailable(self):
        self.is_available = False




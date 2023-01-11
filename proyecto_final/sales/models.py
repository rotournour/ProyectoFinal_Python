from django.db import models
from clothes.models import Type_Clothing

class Payment(models.Model):
    choices = models.CharField(max_length=20)
    
    class Meta():
        db_table = "Payment_method"
        verbose_name = 'Payment'
        verbose_name_plural = 'Payment'

    def __str__(self):
        return self.choices

class Sales(models.Model):
    client = models.CharField(max_length=100, verbose_name= "Cliente")
    clothes_name = models.CharField(max_length=100, verbose_name= "Prenda")
    category = models.ForeignKey(Type_Clothing,null=True,blank=True, on_delete=models.CASCADE, verbose_name='Categoria de la prenda')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name= 'Creacion de la orden')
    payment= models.ForeignKey(Payment, max_length=10, null=True, blank=True, on_delete=models.CASCADE, verbose_name= 'Metodo de pago')
    
    class Meta():
        db_table = "Sales"
        verbose_name = 'Sales'
        verbose_name_plural = 'Sales'



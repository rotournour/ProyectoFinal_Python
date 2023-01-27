from django.db import models


class Payment(models.Model):
    choices = models.CharField(max_length=20)
    
    class Meta():
        db_table = "Payment_method"
        verbose_name = 'Payment'
        verbose_name_plural = 'Payment'

    def __str__(self):
        return self.choices
    


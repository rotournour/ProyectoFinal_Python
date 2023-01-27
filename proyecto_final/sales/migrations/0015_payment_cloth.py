# Generated by Django 4.1.4 on 2023-01-27 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0012_clothes_is_paid'),
        ('sales', '0014_delete_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cloth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clothes.clothes', verbose_name='Prenda pagada'),
        ),
    ]
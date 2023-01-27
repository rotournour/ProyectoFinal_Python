# Generated by Django 4.1.4 on 2023-01-25 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0009_alter_clothes_options_alter_gender_options_and_more'),
        ('sales', '0005_remove_sales_clothes_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='name_clothing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clothes.clothes', verbose_name='Prenda a comprar'),
        ),
    ]

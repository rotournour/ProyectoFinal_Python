# Generated by Django 4.1.4 on 2023-01-27 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0010_rename_stock_clothes_is_available'),
        ('sales', '0011_alter_sales_cloth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='cloth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clothes.clothes', verbose_name='Prenda a comprar'),
        ),
    ]

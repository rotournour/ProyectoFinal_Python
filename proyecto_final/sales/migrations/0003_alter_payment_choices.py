# Generated by Django 4.1.4 on 2023-01-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_payment_alter_sales_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='choices',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-25 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_sales_clothes_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='clothes_name',
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0011_clothes_is_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]

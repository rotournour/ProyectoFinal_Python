# Generated by Django 4.1.4 on 2023-01-10 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0007_alter_clothes_table_alter_gender_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='type_clothing',
            table='Type_of_clothing',
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-26 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_sales_name_clothing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='name_clothing',
            new_name='cloth_id',
        ),
    ]

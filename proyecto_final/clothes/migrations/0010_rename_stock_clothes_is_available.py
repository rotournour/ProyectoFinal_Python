# Generated by Django 4.1.4 on 2023-01-26 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0009_alter_clothes_options_alter_gender_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothes',
            old_name='stock',
            new_name='is_available',
        ),
    ]
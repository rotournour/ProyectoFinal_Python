# Generated by Django 4.1.4 on 2023-01-31 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0018_rename_client_username_clothes_buyer_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='cloth_picture',
            field=models.ImageField(blank=True, null=True, upload_to='clothes_images'),
        ),
    ]

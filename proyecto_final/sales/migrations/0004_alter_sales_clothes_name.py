# Generated by Django 4.1.4 on 2023-01-25 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0009_alter_clothes_options_alter_gender_options_and_more'),
        ('sales', '0003_alter_payment_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='clothes_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clothes.clothes'),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-10 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=30, verbose_name='Tipo de prenda')),
            ],
        ),
        migrations.RemoveField(
            model_name='clothes',
            name='publication',
        ),
        migrations.RemoveField(
            model_name='gender',
            name='gender',
        ),
        migrations.AddField(
            model_name='clothes',
            name='brand',
            field=models.CharField(max_length=50, null=True, verbose_name='Marca de la prenda'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clothes.gender'),
        ),
        migrations.AddField(
            model_name='gender',
            name='genders',
            field=models.CharField(max_length=10, null=True, verbose_name='Genero de la prenda'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre de la prenda'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='new_clothing',
            field=models.BooleanField(verbose_name='Prenda nueva o usada'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='price',
            field=models.FloatField(verbose_name='Precio de la prenda'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clothes.type_clothing'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-10 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='logradouro',
            field=models.CharField(max_length=150, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(verbose_name='Number'),
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-11 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_alter_address_logradouro_alter_address_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['-created_at'], 'verbose_name': 'Address', 'verbose_name_plural': 'Address'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['-created_at'], 'verbose_name': 'City', 'verbose_name_plural': 'Citys'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['-created_at'], 'verbose_name': 'Country', 'verbose_name_plural': 'Countrys'},
        ),
        migrations.AlterModelOptions(
            name='uf',
            options={'ordering': ['-created_at'], 'verbose_name': 'UF', 'verbose_name_plural': 'UFs'},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, verbose_name='City'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-16 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('municipio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='municipios',
            options={'ordering': ['id_municipios'], 'verbose_name': 'Municipio', 'verbose_name_plural': 'Municipios'},
        ),
        migrations.AlterModelTable(
            name='municipios',
            table='Municipios',
        ),
    ]
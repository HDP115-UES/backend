# Generated by Django 4.0.5 on 2022-06-16 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registros',
            options={'ordering': ['usuario'], 'verbose_name': 'Registros', 'verbose_name_plural': 'Registros'},
        ),
        migrations.AlterModelTable(
            name='registros',
            table='Registros',
        ),
    ]

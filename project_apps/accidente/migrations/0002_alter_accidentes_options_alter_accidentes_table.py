# Generated by Django 4.0.5 on 2022-06-16 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accidente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accidentes',
            options={'ordering': ['id_accidente'], 'verbose_name': 'Accidente', 'verbose_name_plural': 'Accidentes'},
        ),
        migrations.AlterModelTable(
            name='accidentes',
            table='Accidentes',
        ),
    ]
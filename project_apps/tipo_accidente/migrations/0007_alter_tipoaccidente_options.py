# Generated by Django 3.2.7 on 2022-06-19 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipo_accidente', '0006_auto_20220618_1846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipoaccidente',
            options={'ordering': ['id_tipo_accidente'], 'verbose_name': 'TipoAccidente', 'verbose_name_plural': 'TipoAccidentes'},
        ),
    ]
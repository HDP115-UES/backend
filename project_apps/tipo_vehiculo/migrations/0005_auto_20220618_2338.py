# Generated by Django 3.2.7 on 2022-06-19 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipo_vehiculo', '0004_alter_tipovehiculo_options_alter_tipovehiculo_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipovehiculo',
            options={'ordering': ['id_tipo_vehiculo'], 'verbose_name': 'TipoVehiculo', 'verbose_name_plural': 'TipoVehiculos'},
        ),
        migrations.AlterField(
            model_name='tipovehiculo',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
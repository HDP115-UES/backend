# Generated by Django 3.2.7 on 2022-06-19 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporte', '0003_auto_20220617_1219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reportes',
            options={'ordering': ['id_reporte'], 'verbose_name': 'Reporte', 'verbose_name_plural': 'Reportes'},
        ),
        migrations.AlterField(
            model_name='reportes',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='posts%Y/%m/%d', verbose_name='Imagen del accidente'),
        ),
        migrations.AlterField(
            model_name='reportes',
            name='numero_involucrados',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

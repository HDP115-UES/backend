# Generated by Django 3.2.7 on 2022-06-19 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accidente', '0003_alter_accidentes_options_alter_accidentes_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accidentes',
            options={'ordering': ['id_accidente'], 'verbose_name': 'Accidente', 'verbose_name_plural': 'Accidentes'},
        ),
        migrations.AlterField(
            model_name='accidentes',
            name='descripción',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

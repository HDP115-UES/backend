# Generated by Django 3.2.7 on 2022-06-19 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporte', '0004_auto_20220618_2338'),
        ('usuario', '0004_auto_20220618_2338'),
        ('registro', '0002_alter_registros_options_alter_registros_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registros',
            options={'ordering': ['id_registros'], 'verbose_name': 'Registro', 'verbose_name_plural': 'Registros'},
        ),
        migrations.AlterField(
            model_name='registros',
            name='reportes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reporte.reportes'),
        ),
        migrations.AlterField(
            model_name='registros',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.usuarios'),
        ),
        migrations.AlterModelTable(
            name='registros',
            table=None,
        ),
    ]

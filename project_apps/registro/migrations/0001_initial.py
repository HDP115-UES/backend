# Generated by Django 4.0.5 on 2022-06-16 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('reporte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id_registros', models.AutoField(primary_key=True, serialize=False)),
                ('reportes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.reportes')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuarios')),
            ],
        ),
    ]

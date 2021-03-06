# Generated by Django 4.0.5 on 2022-06-16 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
        ('accidente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id_reporte', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_accidente', models.DateField(auto_now_add=True)),
                ('hora_accidente', models.TimeField(auto_now_add=True)),
                ('numero_involucrados', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='')),
                ('accidente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accidente.accidentes')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamentos')),
            ],
        ),
    ]

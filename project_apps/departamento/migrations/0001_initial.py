# Generated by Django 4.0.5 on 2022-06-16 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('municipio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id_departamentos', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('Municipios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='municipio.municipios')),
            ],
        ),
    ]

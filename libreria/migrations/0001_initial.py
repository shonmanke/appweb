# Generated by Django 4.1 on 2022-08-10 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('Imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('Autor', models.CharField(max_length=100)),
                ('Genero', models.CharField(max_length=100)),
                ('Año', models.CharField(max_length=100)),
                ('Description', models.TextField(null=True, verbose_name='Descripcion')),
                ('Editorial', models.CharField(max_length=100)),
            ],
        ),
    ]

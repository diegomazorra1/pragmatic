# Generated by Django 3.0.1 on 2020-01-02 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impresora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_pre', models.IntegerField()),
                ('ancho_rodillo', models.IntegerField()),
                ('velocidad_imp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Papel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('costo', models.IntegerField()),
            ],
        ),
    ]

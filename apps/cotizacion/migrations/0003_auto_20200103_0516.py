# Generated by Django 3.0.1 on 2020-01-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0002_auto_20200103_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='costo_operador',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='porc_desperdicio',
            field=models.IntegerField(null=True),
        ),
    ]

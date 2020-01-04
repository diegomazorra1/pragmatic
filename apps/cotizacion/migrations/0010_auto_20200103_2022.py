# Generated by Django 3.0.1 on 2020-01-04 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0009_auto_20200103_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='modo_impresion',
            field=models.CharField(choices=[('a lo largo', 'a lo largo'), ('a lo ancho', 'a lo ancho')], default='a lo largo', max_length=12),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='porc_desperdicio',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=9),
        ),
    ]

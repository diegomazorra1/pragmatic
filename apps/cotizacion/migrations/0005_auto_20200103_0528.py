# Generated by Django 3.0.1 on 2020-01-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0004_auto_20200103_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='costo',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=9),
        ),
    ]

# Generated by Django 3.0.1 on 2020-01-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0005_auto_20200103_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='area',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.0.1 on 2020-01-04 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20200103_0350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='impresora',
            old_name='ancho_rodillo',
            new_name='largo_rodillo',
        ),
    ]
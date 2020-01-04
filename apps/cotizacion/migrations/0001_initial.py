# Generated by Django 3.0.1 on 2020-01-02 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notintas', models.IntegerField()),
                ('ancho', models.IntegerField()),
                ('largo', models.IntegerField()),
                ('tipo_impresion', models.CharField(blank=True, choices=[('Digital', 'Digital'), ('Flexografica', 'Flexografica')], default='Digital', max_length=12, null=True)),
                ('noetiquetas', models.IntegerField()),
                ('porc_utilidad', models.IntegerField()),
                ('costo', models.IntegerField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Cliente')),
                ('maquina_impresion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Impresora')),
                ('tipo_papel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Papel')),
            ],
        ),
    ]
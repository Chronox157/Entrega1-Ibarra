# Generated by Django 4.0.3 on 2022-03-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0003_producto_alter_proveedor_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='celular',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='celular',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-23 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0040_remove_orden_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='productos',
            field=models.ManyToManyField(through='espacios.OrdenProducto', to='espacios.producto'),
        ),
    ]

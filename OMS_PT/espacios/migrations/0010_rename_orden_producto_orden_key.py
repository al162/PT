# Generated by Django 4.2.4 on 2023-09-19 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0009_alter_producto_orden'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='orden',
            new_name='orden_key',
        ),
    ]

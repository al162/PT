# Generated by Django 4.2.4 on 2023-09-19 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0016_rename_productoorden_productorden'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductOrden',
            new_name='ProductoOrden',
        ),
    ]
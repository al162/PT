# Generated by Django 4.2.4 on 2023-09-22 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0028_norden_delete_productorden_remove_orden_productos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductOrden',
        ),
    ]

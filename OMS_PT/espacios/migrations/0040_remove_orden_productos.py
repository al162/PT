# Generated by Django 4.2.4 on 2023-09-23 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0039_ordenproducto_alter_orden_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='productos',
        ),
    ]

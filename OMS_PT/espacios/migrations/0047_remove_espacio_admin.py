# Generated by Django 4.2.4 on 2023-10-27 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0046_espacio_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='espacio',
            name='admin',
        ),
    ]

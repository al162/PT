# Generated by Django 4.2.4 on 2023-09-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0004_alter_producto_espacio_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='espacio_id',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]

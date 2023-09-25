# Generated by Django 4.2.4 on 2023-09-22 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0030_orden_productos_delete_norden'),
    ]

    operations = [
        migrations.CreateModel(
            name='nOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('productos', models.ManyToManyField(to='espacios.producto')),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-23 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0038_orden'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('orden_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espacios.orden')),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espacios.producto')),
            ],
        ),
        migrations.AlterField(
            model_name='orden',
            name='productos',
            field=models.ManyToManyField(through='espacios.OrdenProducto', to='espacios.producto'),
        ),
    ]
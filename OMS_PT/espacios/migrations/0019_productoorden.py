# Generated by Django 4.2.4 on 2023-09-19 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0018_delete_productoorden'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espacios.orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espacios.producto')),
            ],
        ),
    ]
# Generated by Django 4.2.4 on 2023-12-15 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='max_sillas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='min_sillas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='numero',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='mesa_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='sillas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]

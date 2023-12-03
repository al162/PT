# Generated by Django 4.2.4 on 2023-10-27 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('espacios', '0045_remove_espacio_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='espacio',
            name='admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='espacios', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

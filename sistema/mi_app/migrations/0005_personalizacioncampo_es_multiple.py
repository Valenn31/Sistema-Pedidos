# Generated by Django 5.2 on 2025-05-22 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0004_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalizacioncampo',
            name='es_multiple',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 5.1 on 2024-10-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_producto_codigo_alter_producto_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='oculto',
            field=models.BooleanField(default=False),
        ),
    ]
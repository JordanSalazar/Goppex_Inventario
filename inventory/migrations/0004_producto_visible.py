# Generated by Django 5.1 on 2024-10-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_producto_oculto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 5.1 on 2024-10-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_cliente_oculto'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='oculto',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2 on 2024-06-08 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='approved',
            field=models.CharField(default='pending', max_length=255),
        ),
    ]

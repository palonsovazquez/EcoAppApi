# Generated by Django 3.0.6 on 2020-05-21 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cor', '0002_productos_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='code',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

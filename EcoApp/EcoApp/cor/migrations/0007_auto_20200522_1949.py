# Generated by Django 3.0.6 on 2020-05-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cor', '0006_auto_20200522_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-24 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cor', '0018_auto_20200524_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='code',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-22 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cor', '0007_auto_20200522_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='component',
            old_name='id',
            new_name='code',
        ),
    ]

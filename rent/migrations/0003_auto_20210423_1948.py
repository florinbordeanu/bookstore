# Generated by Django 3.1.7 on 2021-04-23 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_auto_20210423_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentbook',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='rentbook',
            name='initial_date',
        ),
    ]

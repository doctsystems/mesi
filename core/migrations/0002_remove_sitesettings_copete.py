# Generated by Django 2.2.15 on 2020-09-18 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='copete',
        ),
    ]

# Generated by Django 2.2.15 on 2020-10-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_dato_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigador',
            name='email',
            field=models.EmailField(default='email@example.com', max_length=254),
        ),
    ]

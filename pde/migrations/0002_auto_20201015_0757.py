# Generated by Django 2.2.15 on 2020-10-15 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pde', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regmip',
            old_name='nacional',
            new_name='grp',
        ),
        migrations.RenameField(
            model_name='regmip',
            old_name='regional',
            new_name='mip',
        ),
        migrations.RenameField(
            model_name='regmip',
            old_name='sector',
            new_name='vbps',
        ),
    ]

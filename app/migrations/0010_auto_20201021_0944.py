# Generated by Django 2.2.15 on 2020-10-21 13:44

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20201008_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actividad',
            old_name='desarrollo',
            new_name='resumen_Abstract',
        ),
        migrations.RenameField(
            model_name='dato',
            old_name='desarrollo',
            new_name='resumen_Abstract',
        ),
        migrations.RenameField(
            model_name='novedad',
            old_name='desarrollo',
            new_name='resumen_Abstract',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='desarrollo',
            new_name='resumen_Abstract',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='desarrollo',
            new_name='resumen_Abstract',
        ),
        migrations.RemoveField(
            model_name='dato',
            name='copete',
        ),
        migrations.RemoveField(
            model_name='novedad',
            name='copete',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='copete',
        ),
        migrations.AddField(
            model_name='dato',
            name='cita_APA',
            field=ckeditor.fields.RichTextField(blank=True, help_text='cita_APA', null=True),
        ),
        migrations.AddField(
            model_name='novedad',
            name='cita_APA',
            field=ckeditor.fields.RichTextField(blank=True, help_text='cita_APA', null=True),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='cita_APA',
            field=ckeditor.fields.RichTextField(blank=True, help_text='cita_APA', null=True),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='doi',
            field=models.URLField(blank=True, help_text='Link s', null=True),
        ),
    ]
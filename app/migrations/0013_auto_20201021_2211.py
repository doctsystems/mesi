# Generated by Django 2.2.15 on 2020-10-22 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_investigadoriiep'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InvestigadorIIEP',
        ),
        migrations.DeleteModel(
            name='ActividadIIEP',
        ),
        migrations.DeleteModel(
            name='ProyectoIIEP',
        ),
        migrations.DeleteModel(
            name='PublicacionIIEP',
        ),
    ]

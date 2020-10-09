# Generated by Django 2.2.15 on 2020-10-08 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20201007_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigador',
            name='email',
            field=models.EmailField(blank=True, default='email@example.com', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='link',
            field=models.URLField(blank=True, help_text='Link al perfil privado', null=True),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='orcid',
            field=models.CharField(blank=True, help_text='Numero ORCID (xxxx-xxxx-xxxx-xxxx)', max_length=30, null=True),
        ),
    ]
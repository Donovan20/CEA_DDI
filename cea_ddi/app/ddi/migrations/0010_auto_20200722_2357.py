# Generated by Django 3.0.7 on 2020-07-23 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddi', '0009_auto_20200722_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingresos',
            name='ingreso',
        ),
        migrations.AddField(
            model_name='proyectos',
            name='ingreso',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-20 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddi', '0005_auto_20200719_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='fecha_respuesta',
            field=models.DateField(blank=True, null=True),
        ),
    ]
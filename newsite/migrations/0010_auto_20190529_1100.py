# Generated by Django 2.0.13 on 2019-05-29 08:00

from django.db import migrations
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsite', '0009_auto_20190529_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=django_bleach.models.BleachField(verbose_name='Краткое описание урока'),
        ),
    ]

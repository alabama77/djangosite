# Generated by Django 2.0.13 on 2019-05-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsite', '0003_auto_20190524_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_category',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

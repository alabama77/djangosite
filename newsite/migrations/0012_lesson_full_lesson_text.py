# Generated by Django 2.0.13 on 2019-05-29 08:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsite', '0011_auto_20190529_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='full_lesson_text',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Полный текст урока'),
            preserve_default=False,
        ),
    ]

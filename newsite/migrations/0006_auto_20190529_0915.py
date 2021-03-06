# Generated by Django 2.0.13 on 2019-05-29 06:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsite', '0005_auto_20190526_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_lesson_text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Название категории', 'verbose_name_plural': 'Названия категорий'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Названия Урока/Лабараторной', 'verbose_name_plural': 'Названия Уроков/Лабараторных'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description_category',
            field=models.TextField(verbose_name='Краткое описание категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Краткое описание урока'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(verbose_name='Ссылка на урок'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.CharField(max_length=150, verbose_name='Преподователь'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовк'),
        ),
    ]

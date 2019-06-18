from django.db import models
from django.conf import settings
from django.utils import timezone
from django.views.generic.edit import FormView
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class Category(models.Model):

	name = models.CharField(max_length=100)
	description_category = models.TextField(
		verbose_name='Краткое описание категории'
		)
	slug = models.SlugField(max_length=50)

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def get_absolute_url(self):
		return reverse('category_detail', kwargs={'category_slug' : self.slug})

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class Lesson(models.Model):

	category = models.ForeignKey(
		'Category',
		on_delete = models.CASCADE,)

	teacher = models.CharField(max_length=150, verbose_name='Преподователь')
	title = models.CharField(max_length=250, verbose_name="Заголовк")
	description = RichTextField(verbose_name='Краткое описание урока')
	full_lesson_text = RichTextUploadingField(verbose_name='Полный текст урока')
	slug = models.SlugField(max_length=50, verbose_name='Ссылка на урок')

	class Meta:

		verbose_name = 'Урок'
		verbose_name_plural = 'Уроки'

	def get_absolute_url(self):
		return reverse('course_template', kwargs={ 'lesson_slug' : self.slug })

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

class Lesson_detail(models.Model):

	full_lesson_text = models.TextField()

	class Meta:
		verbose_name = 'Урок'
		verbose_name_plural = 'Уроки'

	def __unicode__(self):
		return self.full_lesson_text

	def __str__(self):
		return self.full_lesson_text

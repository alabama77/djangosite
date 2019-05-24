from django.db import models
from django.conf import settings
from django.utils import timezone
from django.views.generic.edit import FormView
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from ckeditor.fields import RichTextField


class Category(models.Model):

	name = models.CharField(max_length=100)
	slug = models.SlugField(blank=True)

	def __unicode__(self):
		return self.name

class Lesson(models.Model):

	category = models.ForeignKey(
		'Category', 
		on_delete = models.CASCADE,)

	teacher = models.CharField(max_length=150)
	title = models.CharField(max_length=250)
	description = RichTextField()
	slug = models.SlugField(max_length=50)

	def __unicode__(self):
		return self.name








from django.db import models
from django.conf import settings
from django.utils import timezone
from django.views.generic.edit import FormView
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from ckeditor.fields import RichTextField
from django.urls import reverse


class Category(models.Model):

	name = models.CharField(max_length=100)
	description_category = models.TextField()
	slug = models.SlugField(blank=True)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('coursedetails', kwargs={'lesson_slug' : self.slug})

class Lesson(models.Model):

	category = models.ForeignKey(
		'Category', 
		on_delete = models.CASCADE,)

	teacher = models.CharField(max_length=150)
	title = models.CharField(max_length=250)
	description = models.TextField()
	slug = models.SlugField(max_length=50)

	def __unicode__(self):
		return self.teacher








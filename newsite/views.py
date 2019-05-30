from django.shortcuts import render
from .models import Category, Lesson
# Create your views here.

def index(request):
    return render(request, 'newsite/index.html', {})

def courses(request):

	categories = Category.objects.all()
	context = { "categories" : categories,

				}

	return render(request, 'newsite/courses.html', context)

def categories_view(request, category_slug):

	category = Category.objects.get(slug=category_slug)
	lessons = Lesson.objects.all()

	context = {
		"lessons" : lessons,
		"category" : category,
	}
	return render(request, 'newsite/coursedetails.html', context)

def lessons_view(request, category_slug='algorithms', lesson_slug='algorithms_lesson_1'):

	category = Category.objects.get(slug=category_slug)
	lesson_url = Lesson.objects.get(slug=lesson_slug)
	lessons = Lesson.objects.all()

	context = {
		"lesson_url" : lesson_url,
		"lessons" : lessons,
		"category" : category,
	}
	return render(request, 'newsite/coursedetails.html', context)

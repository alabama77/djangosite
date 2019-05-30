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


def course_view(request, category_slug):

	category = Category.objects.get(slug=category_slug)
	lessons = Lesson.objects.all()
	context = { "category" : category, "lessons" : lessons, }

	return render(request, 'newsite/coursedetails.html', context)

def lesson_view(request, lesson_slug):

	lesson_text = Lesson.objects.all()
	lesson = Lesson.objects.get(slug=lesson_slug)
	context = {'lesson' : lesson, 'lesson_text' : lesson_text,}

	return render(request, 'newsite/coursedetails.html')
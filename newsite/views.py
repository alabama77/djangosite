from django.shortcuts import render, get_object_or_404
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

	category = get_object_or_404(Category, slug=category_slug)
	lessons = Lesson.objects.filter(category__slug__contains=category_slug)
	context = { 
		"category" : category,
		"lessons" : lessons, 
	 	}

	return render(request, 'newsite/coursedetails.html', context)

def lesson_view(request, lesson_slug):

	lesson_text = get_object_or_404(Lesson, slug=lesson_slug)
	context = { 
		'lesson_text' : lesson_text,
		 }

	return render(request, 'newsite/course_template.html', context)
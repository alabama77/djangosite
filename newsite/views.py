from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'newsite/index.html', {})

def courses(request):
	return render(request, 'newsite/courses.html', {})

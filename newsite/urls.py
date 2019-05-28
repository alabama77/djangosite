from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path(r'courses/<str:lesson_slug>/', views.course_details, name='coursedetails'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
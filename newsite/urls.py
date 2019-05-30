from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('courses/<str:category_slug>/', views.course_view, name='category_detail'),
    path('courses/detail/<str:lesson_slug>', views.lesson_view, name='course_template'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path(r'courses/<str:category_slug>/', views.categories_view, name='coursedetails'),
    path(r'courses/<str:category_slug>/<str:lesson_slug>/', views.lessons_view, name='lessons'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path, include
from django.http import HttpResponse
from . import views


def index(request):
    return HttpResponse("This is test")


urlpatterns = [
    path('test/', index),
    path('home/', views.home, ),
    path('about/', views.about, ),
    path('contact/', views.contactmessages),
    path('courses/', views.courses),
    path('newsPortal/', views.newsPortal.as_view(), name='news-portal'),
    path('newsPortal/<int:id>/', views.newsView, name='news-view'),
]

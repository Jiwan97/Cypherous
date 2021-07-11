from django.urls import path, include
from django.http import HttpResponse
from . import views


def index(request):
    return HttpResponse("This is test")


urlpatterns = [
    path('test', index),
    path('home', views.home, ),
    path('about', views.about, ),
    path('contact', views.contact),
    path('courses', views.courses),
]

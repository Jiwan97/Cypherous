from django.urls import path, include
from django.http import HttpResponse
from . import views


def index(request):
    return HttpResponse("This is test")


urlpatterns = [
    path('test/', index),
    path('home/', views.home, ),
    path('', views.home, ),
    path('about/', views.about, ),
    path('contact/', views.contactmessages, name='contact'),
    path('courses/', views.courses),
    path('courseDesk/', views.courseDesk),
    path('newsPortal/', views.newsPortal, name='news-portal'),
    path('newsPortal/category/<slug:slug>', views.tagView),
    path('newsPortal/post-by/<str:username>', views.UserView),
    path('newsPortal/<int:id>/', views.newsView, name='news-view'),
    path('delComments/<int:news_id>/', views.DeleteComments, name='del-com'),
]

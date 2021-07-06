from django.urls import path, include
from django.http import HttpResponse
from . import views


def index(request):
    return HttpResponse("This is test")


urlpatterns = [

    path('home', views.home,),
    path('about', views.about,),
    path('contact', views.contact),
    path('courses', views.courses),
    path('register', views.register,),
    path('login', views.login_user,),
    path('forget-p', views.forget),
    path('logout', views.logoutUser),
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
]

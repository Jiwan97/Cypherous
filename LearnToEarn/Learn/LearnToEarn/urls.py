from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from . import views


def index(request):
    return HttpResponse("This is test")


urlpatterns = [

    path('home', views.home, ),
    path('about', views.about, ),
    path('contact', views.contact),
    path('courses', views.courses),
    path('register', views.register, ),
    path('login', views.login_user, ),
    path('forgot-p', views.forget),
    path('logout', views.logoutUser),
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="LearnToEarn/password_reset.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="LearnToEarn/password_reset_done.html"),
         name="password_reset_complete"),
]

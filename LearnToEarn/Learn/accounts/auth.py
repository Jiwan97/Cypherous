from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return redirect('/admins-dashboard')
        elif request.user.is_authenticated:
            return redirect('/home')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function


def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return view_function(request, *args, **kwargs)
        else:
            return redirect('/home')

    return wrapper_function


def user_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('/admins-dashboard')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function


def nopassyet(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.has_usable_password():
            return redirect('/password_change')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function

from django.shortcuts import render
from accounts.models import Profile


def home(request):
    context = {
            'activate_h': 'active'}
    return render(request, 'LearnToEarn/home.html', context)


def about(request):
    context = {
        'activate_a': 'active'}

    return render(request, 'LearnToEarn/about.html', context)


def courses(request):
    context = {
        'activate_cou': 'active'}
    return render(request, 'LearnToEarn/courses.html', context)


def contact(request):
    context = {
        'activate_c': 'active'}
    return render(request, 'LearnToEarn/contact.html', context)

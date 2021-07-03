from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from .auth import unauthenticated_user
from django.contrib import messages


def home(request):
    return render(request, 'LearnToEarn/home.html')


def about(request):
    return render(request, 'LearnToEarn/about.html')


def courses(request):
    return render(request, 'LearnToEarn/courses.html')


def contact(request):
    return render(request, 'LearnToEarn/contact.html')

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('/login')
        else:
            print(form.errors)
            messages.add_message(request, messages.ERROR,
                                 'Error in registering user')
            return render(request, 'LearnToEarn/register.html', {'form': form})

    context = {'form': form}
    return render(request, 'LearnToEarn/register.html', context)

@unauthenticated_user
def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Invalid username or password')
            return render(request, 'LearnToEarn/login.html')

    return render(request, 'LearnToEarn/login.html', )


def forget(request):
    return render(request, 'LearnToEarn/forgot-password.html')


def logoutUser(request):
    logout(request)
    return redirect('/home')

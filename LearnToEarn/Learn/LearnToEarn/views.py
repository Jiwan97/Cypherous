from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from .auth import unauthenticated_user,user_only

@unauthenticated_user
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form1 = ProfileForm2(request.POST)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user1 = form1.cleaned_data['email']
            Profile.objects.create(user=user, username=user.username, email=user1)
            messages.add_message(request, messages.SUCCESS,
                                 'User registered successfully')
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error in registering user')
            return render(request, 'accounts/register.html', {'form': form})
    context = {
        'form': UserCreationForm,
        'form2': ProfileForm2
    }
    return render(request, 'accounts/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('/')

@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'],
                                password=data['password'])
            if user is not None:
                if not user.is_staff:
                    login(request, user)
                    return redirect('/index')
                elif user.is_staff:
                    login(request, user)
                    return redirect('/admin-dashboard')
            else:
                messages.add_message(request, messages.ERROR,
                                     'Invalid username or password')
                return render(request, 'accounts/login.html', {'form': form})
    context = {
        'form': LoginForm
    }
    return render(request, 'accounts/login.html', context)

@user_only
def user_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Update Successful for' + ' '+str(request.user.profile))
            return redirect('/profile')
    context = {'form': form}

    return render(request, 'accounts/profile.html', context)

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()

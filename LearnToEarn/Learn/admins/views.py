from django.shortcuts import render, redirect
from accounts.auth import admin_only
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseRedirect
from accounts.views import send_response_email
from accounts.models import User
from .forms import NewsForm, ResponseForm
from LearnToEarn.models import News, ContactMessage
from .filters import VFilter
import os



@admin_only
def admin_dashboard(request):
    totalNews = News.objects.all().count()
    users = User.objects.filter(is_staff=False)
    totalmssg = ContactMessage.objects.all().count()
    context = {'users': users,
               'totalNews': totalNews,
               'totalmssg': totalmssg}
    return render(request, 'admins/adminDashboard.html', context)


@login_required
@admin_only
def allNews(request):
    totalNews = News.objects.all().order_by('-id')
    context = {'news': totalNews}
    return render(request, 'admins/allNews.html', context)


@login_required
@admin_only
def newsPost(request):
    form = NewsForm()
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save_m2m()
            messages.success(request, 'News added successfully.')
            return redirect('/admins-dashboard/allNews')

    context = {'form': form}
    return render(request, 'admins/newsPostCreate.html', context)


@login_required
@admin_only
def editnewsPost(request, id):
    newss = News.objects.get(id=id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=newss)
        if form.is_valid():
            form.save()
            messages.success(request, 'News Details updated successfully.')
            return redirect('/admins-dashboard/allNews')

    context = {
        'form': NewsForm(instance=newss),
    }
    return render(request, 'admins/editNewsPost.html', context)


@login_required
@admin_only
def DeletenewsPost(request, id):
    delete = News.objects.get(id=id)
    if delete.news_pic == 'static/images/newsDefault.jpg':
        delete.delete()
    else:
        os.remove(delete.news_pic.path)
        delete.delete()
    return redirect('/admins-dashboard/allNews')


def contactmessage(request):
    totalmsg = ContactMessage.objects.order_by('-id')
    context = {'totalmsg': totalmsg}
    return render(request, 'admins/totalContactMessages.html', context)


def MessageView(request, id):
    form = ContactMessage.objects.get(id=id)
    context = {
        'form': form,
    }
    return render(request, 'admins/VRMessages.html', context)


def Response_(request, id):
    response = ResponseForm()
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            res = form.save(commit=False)
            res.user_id = request.user.id
            res.contactMessage_id = id
            res.save()
            resp = ContactMessage.objects.get(id=id)
            resp.responded = True
            resp.save()
            send_response_email(resp, content, request)
            messages.success(request, 'Response Given successfully')
            return redirect('/admins-dashboard/allContactMessages')

    context = {
        'form': response
    }
    return render(request, 'admins/Response_.html', context)

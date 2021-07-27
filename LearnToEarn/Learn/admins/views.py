from django.shortcuts import render, redirect
from accounts.auth import admin_only
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseRedirect
from accounts.models import User
from .forms import NewsForm
from LearnToEarn.models import News
from .filters import VFilter
import os

@login_required
@admin_only
def admin_dashboard(request):
    totalNews = News.objects.all().count()
    users = User.objects.filter(is_staff=False)
    context = {'users': users,
               'totalNews': totalNews}
    return render(request, 'admins/adminDashboard.html', context)


def allNews(request):
    totalNews = News.objects.all().order_by('-id')
    context = {'news': totalNews}
    return render(request, 'admins/allNews.html', context)


def newsPost(request):
    form = NewsForm()
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/admin-Dashboard')
    else:
        context = {'form': form}
        return render(request, 'admins/newsPostCreate.html', context)


def editnewsPost(request, id):
    newss = News.objects.get(id=id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=newss)
        if form.is_valid():
            form.save()
            messages.success(request, 'News Details updated successfully.')
            return redirect('/admin-dashboard/allNews')

    context = {
        'form': NewsForm(instance=newss),
    }
    return render(request, 'admins/editNewsPost.html', context)


def DeletenewsPost(request, id):
    delete = News.objects.get(id=id)
    os.remove(delete.news_pic.path)
    delete.delete()
    return redirect('/admin-dashboard/allNews')

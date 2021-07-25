from django.shortcuts import render, redirect
from accounts.auth import admin_only
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseRedirect
from accounts.models import User


@login_required
@admin_only
def admin_dashboard(request):
    totalusers = User.objects.filter(is_staff=False).count()
    users = User.objects.filter(is_staff=False)
    context = {'Tusers': totalusers,
               'users': users
               }
    return render(request, 'admins/adminDashboard.html', context)

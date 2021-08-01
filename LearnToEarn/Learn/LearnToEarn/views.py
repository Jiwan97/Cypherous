from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from .models import News, Comment, ContactMessage
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from admins.filters import VFilter


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


# def contact(request):
#     context = {
#         'activate_c': 'active'}
#     return render(request, 'LearnToEarn/contact.html', context)

#
# class newsPortal1(ListView):
#     model = News
#     template_name = 'LearnToEarn/newsPortal.html'
#     context_object_name = 'news'
#     ordering = ['-date_posted']
#     paginate_by = 3


def newsPortal(request):
    form = News.objects.all().order_by('-date_posted')
    tags = News.objects.values_list('Tags', flat=True).distinct()
    pics = News.objects.values_list('news_pic', flat=True).distinct()
    V_filter = VFilter(request.GET, queryset=form)
    V_final = V_filter.qs
    p = Paginator(form, 3)
    page_no = request.GET.get('page', 1)
    page = p.page(page_no)
    context = {
        'form': V_final,
        'news': page,
        'tags': tags,
        'pics': pics,
    }
    return render(request, 'LearnToEarn/NewsPortal.html', context)


def tagView(request, tags):
    form = News.objects.filter(Tags=tags)
    form1 = News.objects.all().order_by('-date_posted')
    V_filter = VFilter(request.GET, queryset=form1)
    V_final = V_filter.qs
    tags = News.objects.values_list('Tags', flat=True).distinct()
    pics = News.objects.values_list('news_pic', flat=True).distinct()
    p = Paginator(form, 3)
    page_no = request.GET.get('page', 1)
    page = p.page(page_no)
    context = {
        'form': V_final,
        'news': page,
        'tags': tags,
        'pics': pics,
    }
    return render(request, 'LearnToEarn/NewsPortal.html', context)


def newsView(request, id):
    if request.method == 'POST':
        comment = request.POST.get('comment-message')
        cmt = Comment.objects.create(comment=comment, user_id=request.user.id, news_id=id)
        if cmt:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        Allnews = News.objects.all().order_by('-date_posted')
        V_filter = VFilter(request.GET, queryset=Allnews)
        V_final = V_filter.qs
        tags = News.objects.values_list('Tags', flat=True).distinct()
        news = News.objects.get(id=id)
        pics = News.objects.values_list('news_pic', flat=True).distinct()
        comments = Comment.objects.filter(news_id=id)
        context = {'news': news,
                   'comments': comments,
                   'pics': pics,
                   'form': V_final,
                   'tags': tags}
        return render(request, 'LearnToEarn/newsView.html', context)


def contactmessages(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            subject = request.POST.get('subject')
            query = request.POST.get('comments')
            message = ContactMessage()
            message.firstname = request.user.profile.firstname
            message.lastname = request.user.profile.lastname
            message.email = request.user.profile.email
            message.phonenumber = request.user.profile.phonenumber
            message.subject = subject
            message.query = query
            message.save()
            messages.success(request, "Message Send successfully. Thank you!")
            return redirect('/contact')
        else:
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            email = request.POST.get('email')
            phonenumber = request.POST.get('phone')
            subject = request.POST.get('subject')
            query = request.POST.get('comments')
            message = ContactMessage()
            message.firstname = firstname
            message.lastname = lastname
            message.email = email
            message.phonenumber = phonenumber
            message.subject = subject
            message.query = query
            message.save()
            messages.success(request, "Message Send successfully. Thank you!")
            return redirect('/contact')

    context = {
        'activate_c': 'active'
    }
    return render(request, 'LearnToEarn/contact.html', context)

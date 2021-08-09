from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import News, Comment, ContactMessage
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
from admins.filters import VFilter
from taggit.models import Tag


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


def courseDesk(request):
    context = {
        'activate_couD': 'active'}
    return render(request, 'LearnToEarn/coursesDescription.html', context)


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
    tags = News.Tags.all()[:13]
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
        'activate_n': 'active',
        'url_next': '?next=/newsPortal',
    }
    return render(request, 'LearnToEarn/NewsPortal.html', context)


def tagView(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    form = News.objects.filter(Tags=tag).order_by('-date_posted')
    form1 = News.objects.all().order_by('-date_posted')
    V_filter = VFilter(request.GET, queryset=form1)
    V_final = V_filter.qs
    tags = News.Tags.all()[:13]
    pics = News.objects.values_list('news_pic', flat=True).distinct()
    p = Paginator(form, 3)
    page_no = request.GET.get('page', 1)
    page = p.page(page_no)
    context = {
        'form': V_final,
        'news': page,
        'tags': tags,
        'pics': pics,
        'activate_n': 'active',
        'url_next': '?next=/newsPortal',
    }
    return render(request, 'LearnToEarn/NewsPortal.html', context)


def newsView(request, id):
    if request.method == 'POST':
        comment = request.POST.get('comment-message')
        cmt = Comment.objects.create(comment=comment, user_id=request.user.id, news_id=id)
        count = Comment.objects.filter(news_id=id).count()
        comment_data = Comment.objects.values().filter(id=cmt.id)
        data = list(comment_data)

        if cmt:
            return JsonResponse(
                {'data': data, 'count': count, 'username': request.user.profile.username,
                 'firstname': request.user.profile.firstname,
                 'lastname': request.user.profile.lastname, 'profile': str(request.user.profile.profile_pic)},
                safe=False)
    else:
        Allnews = News.objects.all().order_by('-date_posted')
        V_filter = VFilter(request.GET, queryset=Allnews)
        V_final = V_filter.qs
        tags = News.Tags.all()[:13]
        news = News.objects.get(id=id)
        pics = News.objects.values_list('news_pic', flat=True).distinct()
        comments = Comment.objects.filter(news_id=id).order_by('-date_commented')
        context = {'news': news,
                   'comments': comments,
                   'pics': pics,
                   'form': V_final,
                   'tags': tags,
                   'activate_n': 'active',
                   'url_next': f'?next=/newsPortal/{id}', }
        return render(request, 'LearnToEarn/newsView.html', context)


def contactmessages(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            subject = request.POST.get('subject')
            query = request.POST.get('comments')
            if subject and query:
                message = ContactMessage()
                message.firstname = request.user.profile.firstname
                message.lastname = request.user.profile.lastname
                message.email = request.user.profile.email
                message.phonenumber = request.user.profile.phonenumber
                message.subject = subject
                message.query = query
                message.save()
                messages.success(request, "Your message has been sent. Your will receive your response shortly. Thank "
                                          "you!")
            else:
                messages.error(request, "You must enter every field to send messages to us")

        else:
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            email = request.POST.get('email')
            phonenumber = request.POST.get('phone')
            subject = request.POST.get('subject')
            query = request.POST.get('comments')
            if firstname and lastname and phonenumber and email and subject and query:
                message = ContactMessage()
                message.firstname = firstname
                message.lastname = lastname
                message.email = email
                message.phonenumber = phonenumber
                message.subject = subject
                message.query = query
                message.save()
                messages.success(request, "Your Message has been sent. Your will receive your response shortly. Thank "
                                          "you!")
            else:
                messages.error(request, "You must enter every field to send messages to us")

    context = {
        'url_next': '?next=/contact',
        'activate_c': 'active'
    }
    return render(request, 'LearnToEarn/contact.html', context)

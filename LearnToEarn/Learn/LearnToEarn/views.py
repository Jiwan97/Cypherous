from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from .models import News, Comment, ContactMessage
from django.http import HttpResponseRedirect
from django.contrib import messages

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


class newsPortal(ListView):
    model = News
    template_name = 'LearnToEarn/newsPortal.html'
    context_object_name = 'news'
    ordering = ['-date_posted']
    paginate_by = 6


def newsView(request, id):
    if request.method == 'POST':
        comment = request.POST['comment-message']

        cmt = Comment.objects.create(comment=comment, user_id=request.user.id, news_id=id)
        if cmt:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        Allnews = News.objects.all().order_by('-id')
        news = News.objects.get(id=id)
        comments = Comment.objects.filter(news_id=id)
        commentsC = Comment.objects.filter(news_id=id).count()
        context = {'news': news,
                   'comments': comments,
                   'count': commentsC,
                   'allnews': Allnews}
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

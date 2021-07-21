from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from .models import News, Comment
from django.http import HttpResponseRedirect


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


class newsPortal(ListView):
    model = News
    template_name = 'LearnToEarn/newsPortal.html'
    context_object_name = 'news'
    ordering = ['-date_posted']
    paginate_by = 4


def newsView(request, id):
    if request.method == 'POST':
        comment = request.POST['comment-message']

        cmt = Comment.objects.create(comment=comment, user_id=request.user.id, news_id=id)
        if cmt:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        news = News.objects.get(id=id)
        comments = Comment.objects.filter(news_id=id)
        commentsC = Comment.objects.filter(news_id=id).count()
        context = {'news': news,
                   'comments': comments,
                   'count': commentsC}
        return render(request, 'LearnToEarn/newsView.html', context)

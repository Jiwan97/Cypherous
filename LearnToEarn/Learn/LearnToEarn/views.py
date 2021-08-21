from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
from admins.filters import *
from .forms import RateForm
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from json import dumps


def home(request):
    context = {
        'activate_h': 'active'}
    return render(request, 'LearnToEarn/home.html', context)


def about(request):
    context = {
        'activate_a': 'active'}

    return render(request, 'LearnToEarn/about.html', context)


@login_required()
def courses(request):
    form = Course.objects.all().order_by('-date')
    V_filter = VFilter1(request.GET, queryset=form)
    V_final = V_filter.qs
    p = Paginator(V_final, 6)
    page_no = request.GET.get('page', 1)
    page = p.page(page_no)
    context = {
        'courses': page,
        'activate_cou': 'active',
        'url_next': '?next=/newsPortal',
    }
    return render(request, 'LearnToEarn/courses.html', context)


@login_required()
def Likedcourses(request):
    likedcourse = Course.objects.filter(courselike__user=request.user).order_by('-date')
    V_filter = VFilter1(request.GET, queryset=likedcourse)
    V_final = V_filter.qs
    p = Paginator(V_final, 6)
    page_no = request.GET.get('page', 1)
    page = p.page(page_no)
    context = {
        'courses': page,
        'activate_cou': 'active',
        'url_next': '?next=/newsPortal',
    }
    return render(request, 'LearnToEarn/courseLike.html', context)


@login_required()
def enrolledCourse(request):
    likedcourse = Course.objects.filter(courseenrollement__user=request.user).order_by('-date')
    V_filter = VFilter1(request.GET, queryset=likedcourse)
    V_final = V_filter.qs
    p = Paginator(V_final, 6)
    page_no = request.GET.get('page', 1)
    page = p.page(page_no)
    context = {
        'courses': page,
        'activate_cou': 'active',
        'url_next': '?next=/newsPortal',
    }
    return render(request, 'LearnToEarn/courses.html', context)


@login_required()
def courseEnrollment(request, course_id):
    if CourseEnrollement.objects.filter(course_id=course_id, user=request.user).exists():
        messages.add_message(request, messages.SUCCESS,
                             'You are already enrolled to this course')
        return redirect(f'/courses/courseDesk/{course_id}')
    else:
        enroll = CourseEnrollement()
        enroll.user = request.user
        enroll.course_id = course_id
        enroll.enrolled = True
        enroll.save()
        messages.add_message(request, messages.SUCCESS,
                             'You have successfully enrolled to this course')
        return redirect(f'/courses/courseDesk/{course_id}')


@login_required()
def courseLike(request):
    course_id = request.GET.get('id', None)
    if CourseLike.objects.filter(course_id=course_id, user=request.user).exists():
        liked = CourseLike.objects.filter(course_id=course_id, user=request.user)
        liked.delete()
        messages.add_message(request, messages.SUCCESS,
                             'This course has been removed from your wishlist')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        liked = CourseLike()
        liked.user = request.user
        liked.course_id = course_id
        liked.like = True
        liked.save()
        messages.add_message(request, messages.SUCCESS,
                             'You have saved this course for later')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def courseDesk(request, course_id):
    if request.method == 'POST':
        if CourseReview.objects.filter(course_id=course_id, user=request.user).exists():
            pass
        else:
            data = CourseReview()
            try:
                rate = int(request.POST.get('rate'))
            except:
                rate = 1
            data.rate = rate
            data.comment = request.POST.get('comment-message')
            data.user = request.user
            data.course_id = course_id
            data.save()
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            count = CourseReview.objects.filter(course_id=course_id).count()
            if count == 0 or count == 1:
                review = "Review"
            else:
                review = "Reviews"
            comment_data = CourseReview.objects.values().get(id=data.pk)
            Avg_data = CourseReview.objects.filter(course_id=course_id).aggregate(Avg('rate'))

            star = '<li><i style="color:#d1d1d1;" class="fa fa-star"></i></li>'
            total_star = ['', star, star, star, star]
            for i in range(0, int(Avg_data['rate__avg'])):
                total_star[i] = '<li><i style="color: #ffc600;" class="fa fa-star"></i></li>'

            star1 = '<li><i style="font-size:12px; color:#d1d1d1;" class="fa fa-star"></i></li>'
            tagstar = ['', star1, star1, star1, star1]
            for i in range(0, comment_data['rate']):
                tagstar[i] = '<li><i style="font-size:12px;" class="fa fa-star"></i></li>'

            poststar_rate = []
            for i in range(0, 5):
                stars = f'<i style="padding-right:5px;" class="fa fa-star  my-btn" id="{i}"></i>'
                poststar_rate.append(stars)
            for i in range(0, comment_data['rate']):
                poststar_rate[i] = f'<i style="padding-right:5px;" class="fa fa-star checked my-btn" id="{i}"></i>'

            return JsonResponse(
                {'data': comment_data, 'review': review, 'count': count, 'username': request.user.profile.username,
                 'tagstar': tagstar, 'poststar_rate': poststar_rate,
                 'firstname': request.user.profile.firstname, 'total_star': total_star,
                 'lastname': request.user.profile.lastname, 'profile': str(request.user.profile.profile_pic)},
                safe=False)

    enrollment = CourseEnrollement.objects.filter(course_id=course_id, user=request.user).exists()
    enrollcount = CourseEnrollement.objects.filter(course_id=course_id).count()
    modulecount = CourseModule.objects.filter(course_id=course_id).count()
    maylike = Course.objects.all().order_by('date')[:3]
    form = Course.objects.get(id=course_id)
    tags = form.category.last()
    related = Course.objects.filter(category=tags).exclude(id=course_id).order_by('-date')[:2]
    lesson = CourseModule.objects.filter(course_id=course_id)
    review_comment = CourseReview.objects.filter(course_id=course_id).order_by('-date_commented')
    can_review = CourseReview.objects.filter(user=request.user, course_id=course_id).exists()
    tagstars = []
    if can_review:
        data = CourseReview.objects.get(user=request.user, course_id=course_id)
        for i in range(0, 5):
            stars = f'<i style="padding-right:5px;" class="fa fa-star  my-btn" id="{i}"></i>'
            tagstars.append(stars)
        print(tagstars)
        for i in range(0, data.rate):
            tagstars[i] = f'<i style="padding-right:5px;" class="fa fa-star checked my-btn" id="{i}"></i>'
        print(tagstars)

    context = {
        'course': form,
        'lesson': lesson,
        'category': tags,
        'enrollment': enrollment,
        'related': related,
        'courselike': maylike,
        'enrollcount': enrollcount,
        'modulecount': modulecount,
        'activate_cou': 'active',
        'url_next': f'?next=/courses/courseDesk/{course_id}',
        'activate_couD': 'active',
        'comments': review_comment,
        'can_review': can_review,
        'tagstars': tagstars
    }

    return render(request, 'LearnToEarn/coursesDescription.html', context)


def editReview(request, course_id):
    comment_edit_data = request.GET.get('commented_data', None)
    try:
        edited_rate = int(request.GET.get('edited_rate'))
    except:
        edited_rate = 1
    review = CourseReview.objects.get(course_id=course_id, user=request.user)
    review.comment = comment_edit_data
    review.rate = edited_rate
    review.edited = True
    review.save()
    data = CourseReview.objects.values().get(course_id=course_id, user=request.user)
    Avg_data = CourseReview.objects.filter(course_id=course_id).aggregate(Avg('rate'))
    star = '<li><i style="color:#d1d1d1;" class="fa fa-star"></i></li>'
    total_star = ['', star, star, star, star]
    for i in range(0, int(Avg_data['rate__avg'])):
        total_star[i] = '<li><i style="color: #ffc600;" class="fa fa-star"></i></li>'

    star1 = '<li><i style="font-size:12px; color:#d1d1d1;" class="fa fa-star"></i></li>'
    tagstar = ['', star1, star1, star1, star1]
    for i in range(0, data['rate']):
        tagstar[i] = '<li><i style="font-size:12px;" class="fa fa-star"></i></li>'

    return JsonResponse(
        {'data': data, 'tagstar': tagstar, 'total_star': total_star,
         },
        safe=False)


def DeleteReview(request, course_id):
    id = request.GET.get('id', None)
    delete = CourseReview.objects.get(id=id)
    delete.delete()
    star = '<li><i style="color:#d1d1d1;" class="fa fa-star"></i></li>'
    loop = 'loop'
    try:
        Avg_data = CourseReview.objects.filter(course_id=course_id).aggregate(Avg('rate'))
        total_star = ['', star, star, star, star]
        for i in range(0, int(Avg_data['rate__avg'])):
            total_star[i] = '<li><i style="color: #ffc600;" class="fa fa-star"></i></li>'
    except Exception:
        total_star = [star, star, star, star, star]
    count = CourseReview.objects.filter(course_id=course_id).count()
    if count == 0 or count == 1:
        review = "Review"
    else:
        review = "Reviews"
    return JsonResponse({'count': count, 'review': review, 'total_star': total_star}, safe=False)


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


def UserView(request, username):
    form = News.objects.filter(user=username).order_by('-date_posted')
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
        comment_data = Comment.objects.values().get(id=cmt.id)
        # data = list(comment_data)
        # print(comment_data)
        if cmt:
            return JsonResponse(
                {'data': comment_data, 'count': count, 'username': request.user.profile.username,
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


def DeleteComments(request, news_id):
    id = request.GET.get('id', None)
    delete = Comment.objects.get(id=id)
    delete.delete()
    count = Comment.objects.filter(news_id=news_id).count()
    return JsonResponse({'count': count}, safe=False)


def Exam(request):
    datas = ExamQNA.objects.values().filter(exammodel_id=1)
    examModel = ExamModel.objects.get(id=1)
    print(examModel.ExamTitle)
    title = examModel.ExamTitle
    data = dumps(list(datas))
    return render(request, 'LearnToEarn/examTest.html', {'questions': data, 'title': title})

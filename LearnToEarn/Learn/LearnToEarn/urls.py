from django.urls import path, include
from django.http import HttpResponse
from . import views


def index(request):
    return HttpResponse("This is test")


urlpatterns = [
    path('test/', index),
    path('home/', views.home, ),
    path('', views.home, ),
    path('about/', views.about, ),
    path('contact/', views.contactmessages, name='contact'),
    path('courses/', views.courses),
    path('likedCourses/', views.Likedcourses),
    path('courseEnrolled/', views.enrolledCourse),
    path('courses/courseDesk/<int:course_id>/', views.courseDesk, name='courseDesk'),
    path('courseEnroll/<int:course_id>/', views.courseEnrollment),
    path('courseLike/', views.courseLike, name='courseLike'),
    path('newsPortal/', views.newsPortal, name='news-portal'),
    path('newsPortal/category/<slug:slug>', views.tagView),
    path('newsPortal/post-by/<str:username>', views.UserView),
    path('newsPortal/<int:id>/', views.newsView, name='news-view'),
    path('delComments/<int:news_id>/', views.DeleteComments, name='del-com'),
    path('delReviews/<int:course_id>/', views.DeleteReview, name='del-rev'),
    path('editReviews/<int:course_id>/', views.editReview, name='edit-rev'),
]


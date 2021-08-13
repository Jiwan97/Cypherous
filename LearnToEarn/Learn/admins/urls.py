from django.urls import path
from admins import views

urlpatterns = [
    path('', views.admin_dashboard),
    path('allNews/', views.allNews),
    path('newsPost/', views.newsPost),
    path('allContactMessages/', views.contactmessage),
    path('messageView/<int:id>/', views.MessageView),
    path('response/<int:id>/', views.Response_),
    path('editNewsPost/<int:id>/', views.editnewsPost),
    path('delNewsPost/<int:id>/', views.DeletenewsPost),
    path('allCourses/', views.allCourses),
    path('CourseCreate/', views.CourseCreate),
    path('allModules/<int:course_id>', views.allModules),
    path('addModule/<int:course_id>', views.ModuleCreate),
    path('editModule/<int:course_id>/<int:module_id>/', views.editModule),
    path('delCourse/<int:course_id>/', views.DeleteCourse),
    path('delModule/<int:course_id>/<int:module_id>/', views.DeleteModule),
]

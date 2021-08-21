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
    path('editCourse/<int:course_id>/', views.editCourse),
    path('allModules/<int:course_id>', views.allModules),
    path('allExams/<int:course_id>', views.allExams),
    path('allQNA/<int:exam_id>', views.allQNA),
    path('addModule/<int:course_id>', views.ModuleCreate),
    path('editModule/<int:course_id>/<int:module_id>/', views.editModule),
    path('delCourse/<int:course_id>/', views.DeleteCourse),
    path('delModule/<int:course_id>/<int:module_id>/', views.DeleteModule),
    path('examCreate/<int:course_id>/', views.ExamCreate, name='exam-create'),
    path('editExam/<int:course_id>/<int:exam_id>/', views.editExam),
    path('delExam/<int:course_id>/<int:exam_id>/', views.DeleteExam),
    path('qnaCreate/<int:exam_id>/', views.QNA),
    path('editQNA/<int:exam_id>/<int:qna_id>/', views.editQNA),
    path('delQNA/<int:exam_id>/<int:qna_id>/', views.DeleteQNA),
]

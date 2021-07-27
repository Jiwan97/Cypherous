from django.urls import path
from admins import views

urlpatterns = [
    path('', views.admin_dashboard),
    path('allNews', views.allNews),
    path('newsPost', views.newsPost),
    path('editNewsPost/<int:id>', views.editnewsPost),
    path('delNewsPost/<int:id>', views.DeletenewsPost),
]

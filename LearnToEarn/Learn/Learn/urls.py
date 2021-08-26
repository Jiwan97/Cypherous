"""Learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from background_task.models import Task
from LearnToEarn.views import timeLapseRepeat
from accounts.processTasks import process_tasks
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LearnToEarn.urls')),
    path('', include('accounts.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    # path('admins-dashboard/', include('admins.urls')),
    # path('', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('admins-dashboard/', include('admins.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not Task.objects.filter(verbose_name="timeLapse").exists():
    timeLapseRepeat(repeat=1, verbose_name="timeLapse")

process_tasks()

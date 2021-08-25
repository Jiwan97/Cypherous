from django.contrib import admin
from .models import *

admin.site.register(News)
admin.site.register(Comment)
admin.site.register(ContactMessage)
admin.site.register(Course)
admin.site.register(CourseModule)
admin.site.register(ExamModel)
admin.site.register(ExamQNA)
admin.site.register(ExamQuestion)
from django.forms import ModelForm, Textarea
from django import forms
from LearnToEarn.models import News, Course, CourseModule
from .models import Response
from taggit.forms import TagWidget


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        exclude = ['user']
        widgets = {
            'Tags': TagWidget(attrs={'data-role': 'tagsinput', })
        }


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = "__all__"
        exclude = ['user', 'contactMessage']


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        exclude = ['user']
        widgets = {
            'category': TagWidget(attrs={'data-role': 'tagsinput', })
        }


class ModuleForm(ModelForm):
    class Meta:
        model = CourseModule
        fields = "__all__"
        exclude = ['course']

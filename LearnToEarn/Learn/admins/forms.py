from django.forms import ModelForm, Textarea
from django import forms
from LearnToEarn.models import News
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

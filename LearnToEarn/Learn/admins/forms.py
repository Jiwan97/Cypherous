from django.forms import ModelForm, Textarea
from django import forms
from LearnToEarn.models import News
from .models import Response


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        exclude = ['user']
        widgets = {
            'news_pic': forms.FileInput(),
            'Tags': forms.TextInput(attrs={'data-role': 'tagsinput', })
        }


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = "__all__"
        exclude = ['user', 'contactMessage']

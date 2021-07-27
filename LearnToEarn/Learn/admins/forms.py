from django.forms import ModelForm, Textarea
from django import forms
from LearnToEarn.models import News


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        exclude = ['user']
        widgets = {
            'news_pic': forms.FileInput()

        }

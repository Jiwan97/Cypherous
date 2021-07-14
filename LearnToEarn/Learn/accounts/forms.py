from django.forms import ModelForm, Textarea
from django import forms
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user', 'username', 'email', 'skills', 'highschool', 'university', 'profile_pic',]


class ProfileForm2(ModelForm):
    class Meta:
        model = Profile
        fields = ['skills', 'highschool', 'university', 'profile_pic']
        widgets = {
            'skills': Textarea(attrs={'cols': 2, 'rows': 2}),
            'profile_pic': forms.FileInput()

        }

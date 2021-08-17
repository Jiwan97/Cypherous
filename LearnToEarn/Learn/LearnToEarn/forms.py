from django.forms import ModelForm, Textarea
from .models import *


class RateForm(ModelForm):
    class Meta:
        model = CourseReview
        fields = ['rate']

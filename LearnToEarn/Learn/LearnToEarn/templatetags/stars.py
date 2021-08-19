from django import template
from LearnToEarn.models import *

register = template.Library()


@register.filter(name='stars')
def stars(id):
    review_comment = CourseReview.objects.get(id=id)
    list = ['', '', '', '', '']
    for i in range(0, review_comment.rate):
        list[i] = i
    return list

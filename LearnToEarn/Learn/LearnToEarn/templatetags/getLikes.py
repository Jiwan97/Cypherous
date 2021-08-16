from django import template
from LearnToEarn.models import *

register = template.Library()


@register.filter(name='getLikes')
def getLikes(id):
    course = Course.objects.get(id=id)
    likes = CourseLike.objects.filter(course=course).count()
    return likes

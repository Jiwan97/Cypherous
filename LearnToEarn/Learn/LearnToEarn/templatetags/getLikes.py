from django import template
from LearnToEarn.models import *

register = template.Library()


@register.filter(name='getLikes')
def getLikes(id):
    likes = CourseLike.objects.filter(course_id=id).count()
    return likes

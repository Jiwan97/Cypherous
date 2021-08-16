from django import template
from LearnToEarn.models import *

register = template.Library()


@register.filter(name='hasLiked')
def hasLiked(request, id):
    course = Course.objects.get(id=id)
    liked = CourseLike.objects.filter(course=course, user=request).exists()
    return liked

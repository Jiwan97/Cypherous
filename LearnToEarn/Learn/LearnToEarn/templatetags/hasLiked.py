from django import template
from LearnToEarn.models import *

register = template.Library()


@register.filter(name='hasLiked')
def hasLiked(request, id):
    liked = CourseLike.objects.filter(course_id=id, user=request).exists()
    return liked

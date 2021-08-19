from django import template
from LearnToEarn.models import CourseReview
from django.db.models import Avg

register = template.Library()


@register.filter(name='getStars')
def getStars(id):
    total = CourseReview.objects.filter(course_id=id).aggregate(Avg('rate'))
    loop = total['rate__avg']
    if loop is not None:
        loop = int(loop)
        list = ['', '', '', '', '']
        for i in range(0, loop):
            list[i] = i
        return list
    else:
        return loop

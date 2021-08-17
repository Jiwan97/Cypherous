from django import template
from LearnToEarn.models import *

register = template.Library()


@register.filter(name='getReview')
def getReview(id):
    count = CourseReview.objects.filter(course_id=id).count()
    return count

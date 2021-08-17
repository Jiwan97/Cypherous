from django import template
from LearnToEarn.models import *

register = template.Library()


@register.filter(name='getEnroll')
def getEnroll(id):
    enrollcount = CourseEnrollement.objects.filter(course_id=id).count()
    return enrollcount

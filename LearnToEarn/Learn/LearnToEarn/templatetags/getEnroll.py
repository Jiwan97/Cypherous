from django import template
from LearnToEarn.models import *

register = template.Library()


@register.filter(name='getEnroll')
def getEnroll(id):
    course = Course.objects.get(id=id)
    enrollcount = CourseEnrollement.objects.filter(course=course).count()
    return enrollcount

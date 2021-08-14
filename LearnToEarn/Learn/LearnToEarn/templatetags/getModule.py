from django import template
from LearnToEarn.models import *

register = template.Library()


@register.filter(name='getModule')
def getModule(id):
    course = Course.objects.get(id=id)
    statement = CourseModule.objects.filter(course=course).exists()
    return statement

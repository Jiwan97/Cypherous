from django import template
from LearnToEarn.models import *

register = template.Library()


@register.filter(name='getModule')
def getModule(id):
    statement = CourseModule.objects.filter(course_id=id).exists()
    return statement

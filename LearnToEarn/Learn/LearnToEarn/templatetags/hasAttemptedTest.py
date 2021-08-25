from django import template
from LearnToEarn.models import *

register = template.Library()


@register.filter(name='hasAttemptedTest')
def hasAttemptedTest(request, id):
    attempt = Attempted.objects.filter(exammodel_id=id, user=request).exists()
    return attempt

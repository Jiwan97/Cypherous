from django import template
from LearnToEarn.models import *

register = template.Library()


@register.filter(name='hasAttemptedExam')
def hasAttemptedExam(request, id):
    exam_id = ExamModel.objects.get(id=id)
    exam_qsn = exam_id.examquestion
    try:
        attempt = ExamAnswer.objects.get(examquestion=exam_qsn, user=request)
    except:
        return False
    return attempt.attempted

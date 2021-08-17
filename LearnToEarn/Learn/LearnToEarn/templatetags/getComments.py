from django import template
from LearnToEarn.models import News, Comment

register = template.Library()


@register.filter(name='getComments')
def getComments(id):
    comment = Comment.objects.filter(news_id=id).count()
    return comment

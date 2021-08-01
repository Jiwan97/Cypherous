from django import template
from LearnToEarn.models import News, Comment

register = template.Library()


@register.filter(name='getComments')
def getComments(id):
    news = News.objects.get(id=id)
    comment = Comment.objects.filter(news=news).count()
    return comment

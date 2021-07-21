from django.db import models
from django.core import validators
from accounts.models import User


class News(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    heading = models.CharField(max_length=200, null=True, default="Not Updated",
                               validators=[validators.MinLengthValidator(4)])
    content = models.TextField( null=True, default="Not Updated",
                               validators=[validators.MinLengthValidator(4)])

    news_pic = models.ImageField("ProfilePic", max_length=500, upload_to='static/uploads',
                                 default='static/images/8.png')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    news = models.ForeignKey(News, null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, null=True, default="Not Updated",
                               validators=[validators.MinLengthValidator(4)])

    date_commented = models.DateTimeField(auto_now_add=True)

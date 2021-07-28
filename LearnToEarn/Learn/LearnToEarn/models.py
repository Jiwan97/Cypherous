from django.db import models
from django.core import validators
from accounts.models import User
from ckeditor.fields import RichTextField


class News(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    heading = models.CharField("Title", max_length=200, null=True, default="Not Updated",
                               validators=[validators.MinLengthValidator(4)])
    content = RichTextField("Put Your Content Here", null=True, default="Not Updated",
                            validators=[validators.MinLengthValidator(4)])

    news_pic = models.ImageField("News Pic", max_length=500, upload_to='static/uploads',
                                 default='static/images/newsDefault.jpg')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    news = models.ForeignKey(News, null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, null=True, default="Not Updated",
                               validators=[validators.MinLengthValidator(4)])

    date_commented = models.DateTimeField(auto_now_add=True)


class ContactMessage(models.Model):
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phonenumber = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    query = models.CharField(max_length=1000, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname

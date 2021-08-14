from django.db import models
from django.core import validators
from accounts.models import User
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class News(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    heading = models.CharField("Title", max_length=200, null=True, default="Not Updated",
                               validators=[validators.MinLengthValidator(4)])
    content = RichTextField("Put Your Content Here", null=True, default="Not Updated",
                            validators=[validators.MinLengthValidator(4)])

    news_pic = models.ImageField("News Pic", max_length=500, upload_to='static/uploads',
                                 default='static/images/newsDefault.jpg')
    date_posted = models.DateTimeField(auto_now_add=True)

    Tags = TaggableManager()

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


class Course(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    course_name = models.CharField("Course Name", max_length=200, null=True, default="Not Updated",
                                   validators=[validators.MinLengthValidator(4)])
    course_summary = models.CharField("Course Summary", max_length=200, null=True, default="Not Updated",
                                      validators=[validators.MinLengthValidator(4)])
    to_learn = RichTextField("What students needs to learn before joining this course", max_length=50000, null=True,
                             default="You can join this course right away",
                             )
    course_pic = models.ImageField("Course Pic", max_length=500, upload_to='static/uploads',
                                   default='static/images/newsDefault.jpg')
    date = models.DateTimeField(auto_now_add=True, null=True)
    category = TaggableManager()

    def __str__(self):
        return self.course_name


class CourseEnrollement(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    enrolled = models.BooleanField(default=False)

    def __str__(self):
        return self.enrolled


class CourseModule(models.Model):
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    modulenumber = models.IntegerField('Lecture Number', null=True
                                       )
    module = models.CharField('Module Name', max_length=200, null=True,
                              validators=[validators.MinLengthValidator(4)])

    ModuleLecture = RichTextField('Module Lecture', max_length=50000, null=True,
                                  validators=[validators.MinLengthValidator(4)])

    def __str__(self):
        return self.module

    class Meta:
        ordering = ('modulenumber',)


class CourseReview(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, null=True, default="Not Updated",
                               validators=[validators.MinLengthValidator(4)])

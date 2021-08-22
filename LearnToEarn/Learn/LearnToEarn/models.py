from django.db import models
from django.core import validators
from accounts.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
import readtime
from django.db.models import Avg


class News(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    heading = models.CharField("Title", max_length=200, null=True, default="Not Updated",
                               validators=[validators.MinLengthValidator(4)])
    content = RichTextUploadingField("Put Your Content Here", null=True, default="Not Updated",
                                     validators=[validators.MinLengthValidator(4)])

    news_pic = models.ImageField("News Pic", max_length=500, upload_to='static/uploads',
                                 default='static/images/newsDefault.jpg')
    date_posted = models.DateTimeField(auto_now_add=True)

    Tags = TaggableManager()

    def __str__(self):
        return self.heading

    def getComments(self):
        comment = Comment.objects.filter(news_id=self.pk).count()
        return comment


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
                                   )
    course_summary = models.CharField("Course Summary", max_length=200, null=True, default="Not Updated",
                                      )
    to_learn = RichTextField("What students needs to learn before joining this course", max_length=50000, null=True,
                             default="You can join this course right away",
                             )
    course_pic = models.ImageField("Course Pic", max_length=500, upload_to='static/uploads',
                                   default='static/images/slider-01.jpg')
    date = models.DateTimeField(auto_now_add=True, null=True)
    category = TaggableManager()

    def __str__(self):
        return self.course_name

    def getStars(self):
        total = CourseReview.objects.filter(course_id=self.pk).aggregate(Avg('rate'))
        loop = total['rate__avg']
        if loop is not None:
            dec = str(loop - int(loop))[2:]
            if '0' == dec:
                loop = int(loop)
                list = ['', '', '', '', '']
                for i in range(0, loop):
                    list[i] = i
                return list
            else:
                loop = int(loop)
                list = ['', '', '', '', '']
                for i in range(0, loop):
                    list[i] = i
                list[loop] = 'half'
                return list

        else:
            return loop

    def getEnroll(self):
        enrollcount = CourseEnrollement.objects.filter(course_id=self.pk).count()
        return enrollcount

    def getLikes(self):
        likes = CourseLike.objects.filter(course_id=self.pk).count()
        return likes

    def getReview(self):
        count = CourseReview.objects.filter(course_id=self.pk).count()
        return count

    def getModule(self):
        statement = CourseModule.objects.filter(course_id=self.pk).exists()
        return statement

    def hasLiked(self, user):
        liked = CourseLike.objects.filter(course_id=self.pk, user=user).exists()
        return liked


class CourseEnrollement(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    enrolled = models.BooleanField(default=False)


class CourseLike(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    like = models.BooleanField(default=False)


class CourseModule(models.Model):
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    modulenumber = models.IntegerField('Lecture Number', null=True
                                       )
    module = models.CharField('Module Name', max_length=200, null=True,
                              )

    ModuleLecture = RichTextUploadingField('Module Lecture', max_length=50000, null=True,
                                           )

    def __str__(self):
        return self.module

    class Meta:
        ordering = ('modulenumber',)

    def get_readtime(self):
        result = readtime.of_text(self.ModuleLecture)
        return result.text


Rate_Choice = [
    (1, '1-Star'),
    (2, '2-Star'),
    (3, '3-Star'),
    (4, '4-Star'),
    (5, '5-Star'),
]


class CourseReview(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50000, null=True, default="Not Updated",
                               )
    rate = models.PositiveSmallIntegerField("Choose Your Rating", choices=Rate_Choice)
    edited = models.BooleanField(default=False)
    date_commented = models.DateTimeField(auto_now_add=True)

    def stars(self):
        list = ['', '', '', '', '']
        for i in range(0, self.rate):
            list[i] = i
        return list


class ExamModel(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    ExamNumber = models.PositiveSmallIntegerField('Exam Number', null=True
                                                  )
    ExamTitle = models.CharField('Title', max_length=500, null=True, default="Not Updated",
                                 )
    date = models.DateTimeField(auto_now_add=True)


class Attempted(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    exammodel = models.ForeignKey(ExamModel, null=True, on_delete=models.CASCADE)
    date_attempted = models.DateTimeField(auto_now_add=True)
    attempted = models.BooleanField(default=False)
    user_score = models.PositiveSmallIntegerField("Score", default=0)


class ExamQNA(models.Model):
    exammodel = models.ForeignKey(ExamModel, null=True, on_delete=models.CASCADE)
    numb = models.PositiveSmallIntegerField("Number", default=0)
    question = models.CharField(max_length=5000, null=True)
    option1 = models.CharField("Option 1", max_length=5000, null=True)
    option2 = models.CharField("Option 2", max_length=5000, null=True)
    option3 = models.CharField("Option 3", max_length=5000, null=True)
    option4 = models.CharField("Option 4", max_length=5000, null=True)
    answer = models.CharField("Answer", max_length=5000, null=True)

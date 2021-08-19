from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators


class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True)
    firstname = models.CharField("First Name", default="Name not Updated", max_length=200, null=True,
                                 validators=[validators.MinLengthValidator(4)])
    lastname = models.CharField("Last Name", default="", max_length=200, null=True,
                                validators=[validators.MinLengthValidator(4)])
    birthdate = models.DateField("Birth Date", null=True, blank=True, default=None)
    country = models.CharField(max_length=200, null=True, default="Not Updated",
                               validators=[validators.MinLengthValidator(4)])
    address = models.CharField(max_length=200, null=True, default="Not Updated",
                               validators=[validators.MinLengthValidator(4)])
    phonenumber = models.CharField("Phone Number", max_length=200, null=True, default="Not Updated",
                                   validators=[validators.MaxLengthValidator(10)])
    facebooklink = models.CharField("Facebook Link", max_length=200, null=True, default="Not Updated",
                                    validators=[validators.MinLengthValidator(4)])
    skills = models.CharField(max_length=200, null=True, default="Not Updated",
                              validators=[validators.MinLengthValidator(4)])
    university = models.CharField(max_length=200, null=True,
                                  default="Not Updated", validators=[validators.MinLengthValidator(4)])
    highschool = models.CharField("High School", max_length=200, null=True,
                                  default="Not Updated", validators=[validators.MinLengthValidator(4)])

    gender = models.CharField(max_length=200, default="Not Updated", null=True,
                              validators=[validators.MaxLengthValidator(6)])
    email = models.EmailField(max_length=200, default="Not Updated", null=True, validators=[validators.validate_email])
    occupation = models.CharField(max_length=200, default="Not Updated", null=True,
                                  validators=[validators.MinLengthValidator(3)])
    profile_pic = models.ImageField("ProfilePic", max_length=500, upload_to='static/uploads',
                                    default='static/images/8.png')
    created_date = models.DateTimeField(auto_now_add=True)
    sendNotification = models.BooleanField("Send Login Notification", default=True)

    def __str__(self):
        return self.username

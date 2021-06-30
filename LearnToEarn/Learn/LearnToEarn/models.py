from django.db import models
from django.contrib.auth.models import User
from django.core import validators


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True)
    firstname = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(4)])
    lastname = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(4)])
    phone = models.CharField(max_length=200, null=True, validators=[validators.MaxLengthValidator(10)])
    email = models.EmailField(max_length=200, null=True, validators=[validators.validate_email])
    profile_pic = models.FileField(upload_to='static/uploads',
                                   default='static/images/8.png')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
from django.db import models
from django.core import validators
from ckeditor.fields import RichTextField
from LearnToEarn.models import User, ContactMessage


class Response(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    contactMessage = models.ForeignKey(ContactMessage, null=True, on_delete=models.CASCADE)
    content = RichTextField("Your Response Here", null=True, default="Not Updated",
                            validators=[validators.MinLengthValidator(4)])

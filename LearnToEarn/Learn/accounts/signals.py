from django.db.models.signals import post_save
from .models import User, Profile
from django.dispatch import receiver
from LearnToEarn.models import News


@receiver(post_save, sender=User)
def profile_creation(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.username, email=instance.email)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

#
# @receiver(post_save, sender=News)
# def save_news(request, sender, instance, created, **kwargs):
#     instance.user = request.user
#     instance.save()

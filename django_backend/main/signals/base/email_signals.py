from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from social_django import BaseAuth
from main.models import BaseUser


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        # BaseUser.objects.create(username=kwargs['instance'])
        print("success")

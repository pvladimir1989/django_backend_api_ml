from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save


def create_profile(sender, **kwargs):
    if kwargs['created']:
        # User.objects.create(username=kwargs['instance'])
        print("success")


post_save.connect(create_profile, sender=User)

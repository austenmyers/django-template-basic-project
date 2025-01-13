from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import UserAccount, UserProfile


@receiver(post_save, sender=UserAccount)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

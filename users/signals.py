from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import ExtraData


@receiver(post_save, sender=User)
def create_extradata(sender, instance, created, **kwargs):
    if created:
        ExtraData.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_extradata(sender, instance, **kwargs):
    instance.extradata.save()

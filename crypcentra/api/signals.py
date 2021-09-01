from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta

from .models import Coins
from .tasks import assign_token_to_user


@receiver(post_save, sender=Coins)
def create_coin(sender, instance, created, **kwargs):
    if created:
        assign_token_to_user.apply_async(eta=instance.end_time)

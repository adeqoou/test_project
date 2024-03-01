from datetime import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


# Распределение по группам после сохранения
@receiver(post_save, sender=Product)
def member_distribute(sender, instance, **kwargs):
    if kwargs['created']:
        if instance.start_date > timezone.now():
            groups = Group.objects.filter(product=instance)
            members_count = Members.objects.filter(group__in=groups).count()
            max_group_size = members_count // groups.count()
            remainder = members_count % groups.count()

            for group in groups:
                participants = group.participant_set.all()
                if participants.count() < max_group_size:
                    group.participant_set.create(user=instance.creator)
                    return
            for group in groups:
                if group.participant_set.all().count() < max_group_size + 1:
                    group.participant_set.create(user=instance.creator)
                    return group.participant_set.create(user=instance.creator)
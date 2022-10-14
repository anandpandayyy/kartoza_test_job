from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    permission1 = Permission.objects.get(name="Can view user")
    permission2 = Permission.objects.get(name="Can change user")
    if created and instance.is_active:
        if instance.is_staff == False:
            instance.is_staff = True
            instance.save()
    else:
        instance.user_permissions.add(permission1)
        instance.user_permissions.add(permission2)

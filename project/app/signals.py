from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import ADDITION, CHANGE, DELETION, LogEntry

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    """
    For permision and add useer to is_staff
    """
    permission1 = Permission.objects.get(name="Can view user")
    permission2 = Permission.objects.get(name="Can change user")
    if created and instance.is_active:
        if not instance.is_staff:
            instance.is_staff = True
            instance.save()
    else:
        instance.user_permissions.add(permission1)
        instance.user_permissions.add(permission2)


def add_log_entry(request, flag):
    """
    add entry of login and logout of users
    """
    LogEntry.objects.log_action(
        user_id=request.user.id,
        content_type_id=ContentType.objects.get(model="logentry").id,
        object_id=request.user.id,
        object_repr=request.user.username,
        action_flag=flag,
    )


@receiver(user_logged_in)
def user_login_logentry(sender, request, user, **kwargs):
    """
    Check user login activity
    """
    flag = ADDITION if user_logged_in else CHANGE
    add_log_entry(request, flag)


@receiver(user_logged_out)
def user_logout_logentry(sender, request, user, **kwargs):
    """
    Check user logout activity
    """
    flag = DELETION if user_logged_out else CHANGE
    add_log_entry(request, flag)

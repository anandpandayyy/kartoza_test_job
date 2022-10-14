# from django.contrib.gis.db import models

from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='profile_images/')
    phone_number = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    address = models.TextField(max_length=500, blank=True)
    # location = models.MultiPolygonField()

    def __str__(self):
        return self.username

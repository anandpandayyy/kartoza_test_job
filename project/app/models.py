from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django_admin_geomap import GeoItem
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, GeoItem):
    """
    abstracted user model and added geo map
    """
    image = models.ImageField(upload_to="static/profile_images/")
    phone_number = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    address = models.TextField(max_length=500, blank=True)
    lon = models.FloatField(default=95.1849)  # longitude
    lat = models.FloatField(default=64.2637)  # latitude

    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)

    @property
    def geomap_icon(self):
        """
        Icon sign showing in map
        """
        return self.default_icon

    @property
    def geomap_popup_view(self):
        """
        template showing while clicking on icon
        """
        return "<img src='/static/profile.png' alt='img' height=50px;\
            width=40px> <br> <span><b> Username: </b> {} </span> <br> \
            <span><b> Address: </b> {} </span> <br> \
            <span> <b> Phone Number: </b> {} </span> <br> \
            <span> <b>Lat: </b> {} </span> <br> \
            <span> <b>Long: </b> {} </span>  ".format(
            str(self.username),
            str(self.address),
            str(self.phone_number),
            str(self.lat),
            str(self.lon),
        )

    @property
    def geomap_popup_edit(self):
        """
        opening when a particular user want to change their location
        """
        return self.geomap_popup_view

    def __str__(self):
        return self.username

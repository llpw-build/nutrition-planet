from django.db import models
from django.conf import settings 

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_profile",
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    address_line_1 = models.CharField(
        max_length=200,
        blank=True,
    )

    address_line_2 = models.CharField(
        max_length=200,
        blank=True,
    )

    town_or_city = models.CharField(
        max_length=50,
        blank=True,
    )

    postcode = models.CharField(
        max_length=20,
        blank=True,
    )

    country = models.CharField(
        max_length=50,
        blank=True,
    )
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    friendly_name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.friendly_name

class Brand(models.Model):
    slug = models.SlugField(
        max_length=100,
        unique=True,
    )

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    logo = models.ImageField(
        upload_to="brands/logos/",
    )

    website = models.URLField(
        blank=True,
    )

    def __str__(self):
        return self.name
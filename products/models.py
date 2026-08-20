from django.db import models
from django.contrib.auth.models import User

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


class Product(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name="products",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    size_or_quantity = models.CharField(
        max_length=100,
    )

    materials = models.TextField(
        blank=True
    )

    ingredients = models.TextField(
        blank=True
    )

    stock_quantity = models.PositiveIntegerField(
        default=0
    )

    description = models.TextField(
        blank=True,
    )

    image = models.ImageField(
        upload_to="products/images/",
    )

    is_active= models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name

class Review(models.Model):

    RATING_CHOICES = [
        (1, "1 Star"),
        (2, "2 Stars"),
        (3, "3 Stars"),
        (4, "4 Stars"),
        (5, "5 Stars"),
    ]

    product = models.ForeignKey(
    Product,
    on_delete=models.CASCADE,
    related_name="reviews",
    )

    product = models.ForeignKey(
    Product,
    on_delete=models.CASCADE,
    related_name="reviews",
    )

    comment = models.TextField()

    rating = models.IntegerField(
    choices=RATING_CHOICES,
    )

    date = models.DateTimeField(
    auto_now_add=True,
    )

    def __str__(self):
        return f"{self.user} - {self.product} - {self.rating}"

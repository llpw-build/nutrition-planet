from django.db import models
from products.models import Product
from profiles.models import UserProfile
# Create your models here.


class Order(models.Model):

    full_name = models.CharField(
        max_length=100,
    )

    email = models.EmailField(
        max_length=254,
    )

    phone_number = models.CharField(
        max_length=20,
    )

    street_address = models.CharField(
        max_length=100,
    )

    town_or_city = models.CharField(
        max_length=100,
    )

    postcode = models.CharField(
        max_length=20,
    )

    country = models.CharField(
        max_length=100,
    )

    date = models.DateTimeField(
    auto_now_add=True,
    )

    order_total = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
    )

    payment_status = models.CharField(
    max_length=10,
    default="pending",
    )

    profile = models.ForeignKey(
    UserProfile,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="orders",
    )


    stripe_payment_intent_id = models.CharField(
    max_length=255,
    blank=True,
    null=True,
    unique=True,
    )

    def update_total(self):
        self.order_total = sum(
            item.lineitem_total
            for item in self.lineitems.all()
        )

        self.save()

    def __str__(self):
        return f"Order {self.id} - {self.full_name}"


class OrderLineItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="order_line_items",
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    lineitem_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    def save(self, *args, **kwargs):
        self.lineitem_total = (
            self.product.price * self.quantity
        )

        super().save(*args, **kwargs)

        self.order.update_total()

    def delete(self, *args, **kwargs):
        order = self.order

        super().delete(*args, **kwargs)

        order.update_total()

    def __str__(self):
        return (
            f"{self.quantity} x {self.product.name} "
            f"on order {self.order.id}"
        )
    

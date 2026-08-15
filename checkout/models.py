from django.db import models
from products.models import Product
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

    def __str__(self):
        return (
            f"{self.quantity} x {self.product.name} "
            f"on order {self.order.id}"
    )

    

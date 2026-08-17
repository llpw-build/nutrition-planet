from django.test import TestCase
from django.urls import reverse
from products.models import Brand, Category, Product
from .models import Order, OrderLineItem

# Create your tests here.

class CheckoutTests(TestCase):

    def setUp(self):
        self.brand = Brand.objects.create(
            slug="test-brand",
            name="Test Brand",
        )

        self.category = Category.objects.create(
            name="test-category",
            friendly_name="Test Category",
        )

        self.product = Product.objects.create(
            name="Test Product",
            brand=self.brand,
            category=self.category,
            price="10.00",
            size_or_quantity="1 item",
            stock_quantity=10,
            image="products/images/test.jpg",
            is_active=True,
        )

        session = self.client.session
        session["bag"] = {
            str(self.product.id): 2,
        }
        session.save()

    def test_checkout_creates_order(self):

        self.client.post(
            reverse("checkout"),
            {
                "full_name": "Test User",
                "email": "test@example.com",
                "phone_number": "07700900123",
                "street_address": "1 Test Street",
                "town_or_city": "Newport",
                "postcode": "NP20 1AA",
                "country": "United Kingdom",
            },
        )

        self.assertEqual(
            Order.objects.count(),
            1,
        )


    def test_checkout_creates_order_line_item(self):

        self.client.post(
            reverse("checkout"),
            {
                "full_name": "Test User",
                "email": "test@example.com",
                "phone_number": "07700900123",
                "street_address": "1 Test Street",
                "town_or_city": "Newport",
                "postcode": "NP20 1AA",
                "country": "United Kingdom",
            },
        )

        line_item = OrderLineItem.objects.first()

        self.assertEqual(
            line_item.product,
            self.product,
        )

        self.assertEqual(
            line_item.quantity,
            2,
        )

    def test_checkout_clears_bag(self):

        self.client.post(
            reverse("checkout"),
            {
                "full_name": "Test User",
                "email": "test@example.com",
                "phone_number": "07700900123",
                "street_address": "1 Test Street",
                "town_or_city": "Newport",
                "postcode": "NP20 1AA",
                "country": "United Kingdom",
            },
        )

        session = self.client.session

        self.assertNotIn(
            "bag",
            session,
        )
from django.test import TestCase
from django.urls import reverse 
from .models import Product, Brand, Category

# Create your tests here.

class ProductTests(TestCase):

    def test_str_returns_product_name(self):
        brand = Brand.objects.create(
            slug="optimum-nutrition",
            name="Optimum Nutrition",
            logo="brands/logos/optimum-nutrition.jpg",
        )

        category = Category.objects.create(
            name="protein-powder",
            friendly_name="Protein Powder",
        )

        product = Product.objects.create(
            name="Gold Standard Whey",
            brand=brand,
            category=category,
            price="29.99",
            size_or_quantity="1 kg",
            image="products/images/gold-standard-whey.jpg",
        )

        self.assertEqual(
            str(product),
            "Gold Standard Whey",
        )

    def test_products_page_returns_200(self):
        response = self.client.get(reverse("all_products"))

        self.assertEqual(
            response.status_code,
            200,
        )


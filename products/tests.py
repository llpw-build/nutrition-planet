from django.test import TestCase
from django.urls import reverse 
from .models import Product, Brand, Category
from django.contrib.auth import get_user_model

# Create your tests here.

class ProductTests(TestCase):

    def setUp(self):
        self.brand = Brand.objects.create(
            slug="optimum-nutrition",
            name="Optimum Nutrition",
            logo="brands/logos/optimum-nutrition.jpg",
        )

        self.category = Category.objects.create(
            name="protein-powder",
            friendly_name="Protein Powder",
        )

        self.other_category = Category.objects.create(
            name="creatine",
            friendly_name="Creatine",
        )

        self.product = Product.objects.create(
            name="Gold Standard Whey",
            brand=self.brand,
            category=self.category,
            price="29.99",
            size_or_quantity="1 kg",
            image="products/images/gold-standard-whey.jpg",
        )

        self.other_product = Product.objects.create(
            name="Creatine Monohydrate",
            brand=self.brand,
            category=self.other_category,
            price="19.99",
            size_or_quantity="500 g",
        )

        self.inactive_product = Product.objects.create(
            name="Inactive Test Product",
            brand=self.brand,
            category=self.category,
            price="9.99",
            size_or_quantity="250 g",
            is_active=False,
        )

    def test_str_returns_product_name(self):

        self.assertEqual(
            str(self.product),
            "Gold Standard Whey",
        )

    def test_products_page_returns_200(self):
        response = self.client.get(reverse("all_products"))

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_products_detail_page_returns_200(self):
        response = self.client.get(
            reverse(
                "product_detail",
                kwargs={
                "product_id": self.product.id,
            },
        )
    )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")
        self.assertContains(response, "Gold Standard Whey")

    def test_search_returns_matching_products(self):
        response = self.client.get(
            reverse("all_products"),
            {"q": "whey"},
    )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            "Gold Standard Whey",
        )

        self.assertNotContains(
        response,
        "Creatine Monohydrate",
    )

    def test_category_filter_returns_matching_products(self):
        response = self.client.get(
            reverse("all_products"),
            {"category": "protein-powder"},
    )

        self.assertContains(
            response,
            "Gold Standard Whey",
    )

        self.assertNotContains(
            response,
            "Creatine Monohydrate",
        )

    def test_products_sort_by_price_ascending(self):
        response = self.client.get(
            reverse("all_products"),
            {
             "sort": "price",
             "direction": "asc",
        },
    )

        products = list(response.context["products"])

        self.assertEqual(
            products,
            [self.other_product, self.product],
        )

    def test_inactive_products_are_not_displayed(self):
        response = self.client.get(reverse("all_products"))

        self.assertContains(
        response,
        "Gold Standard Whey",
        )

        self.assertNotContains(
        response,
        "Inactive Test Product",
        )

    def test_invalid_product_id_returns_404(self):
        response = self.client.get(
            reverse(
                "product_detail",
                kwargs={
                    "product_id": 999999,
                },
            )
        )

        self.assertEqual(
            response.status_code,
            404,
        )

class ProductCreateTests(TestCase):

    def test_staff_user_can_access_add_product(self):
        User = get_user_model()

        user = User.objects.create_user(
            username="staffuser",
            password="testpass123",
            is_staff=True,
        )

        self.client.login(
            username="staffuser",
            password="testpass123",
        )

        response = self.client.get(
            reverse("add_product")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_not_staff_user_can_access_add_product(self):
            User = get_user_model()
    
            user = User.objects.create_user(
                username="staffuser",
                password="testpass123",
                is_staff=False,
            )
    
            self.client.login(
                username="staffuser",
                password="testpass123",
            )
    
            response = self.client.get(
                reverse("add_product")
            )
    
            self.assertEqual(
                response.status_code,
                302,
            )
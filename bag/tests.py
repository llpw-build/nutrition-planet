from django.test import TestCase
from django.urls import reverse
from products.models import Brand, Category, Product


class BagTests(TestCase):

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

    def test_add_to_bag_adds_product_to_session(self):

        self.client.post(
            reverse(
                "add_to_bag",
                args=[self.product.id],
            ),
            {
                "quantity": 2,
            },
        )

        bag = self.client.session["bag"]

        self.assertEqual(
            bag[str(self.product.id)],
            2,
        )

    def test_update_bag_replaces_quantity(self):

        session = self.client.session
        session["bag"] = {
            str(self.product.id): 4,
    }
        session.save()

        self.client.post(
           reverse(
                "update_bag",
                args=[self.product.id],
            ),
            {
            "quantity": 2,
            },
        )

        bag = self.client.session["bag"]

        self.assertEqual(
            bag[str(self.product.id)],
            2,
        )

    def test_remove_from_bag_removes_product(self):

        session = self.client.session
        session["bag"] = {
            str(self.product.id): 2,
        }
        session.save()

        self.client.post(
            reverse(
                "remove_from_bag",
                args=[self.product.id],
            )
        )

        bag = self.client.session["bag"]

        self.assertNotIn(
            str(self.product.id),
            bag,
        )
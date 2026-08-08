from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TestHomeView(TestCase):

    def home_page_load_test(self):

        response = self.client.get(reverse("home"))
              
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "main/index.html")

        self.assertContains(response, "Planet Nutrition")
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class RegisterTests(TestCase):

    def test_registration_page_returns_200(self):

        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html",)
        self.assertContains(response,"Register",)

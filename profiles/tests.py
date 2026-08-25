from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.


class RegisterTests(TestCase):

    def test_registration_page_returns_200(self):

        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html",)
        self.assertContains(response, "Register",)


class UserProfileTests(TestCase):
    def test_logged_in_user_can_access_profile(self):
        User = get_user_model()

        user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )

        self.client.login(
            username="testuser",
            password="testpass123",
        )

        response = self.client.get(
            reverse("profile")
        )

    def test_anonymous_user_cannot_access_profile(self):
        response = self.client.get(
            reverse("profile")
        )

        self.assertEqual(
            response.status_code,
            302,
        )

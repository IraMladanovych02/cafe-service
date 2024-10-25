from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="admin12345"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="test12345",
            years_of_experience=16,
        )

    def test_cook_years_of_experience_listed(self):
        """
        Test that cook's years of experience is in list_display
        on cook admin page
        """
        url = reverse("admin:cafe_cook_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.cook.years_of_experience)

    def test_cook_detail_years_of_experience_listed(self):
        """
        Test that cook's years of experience is on cook detail admin page
        """
        url = reverse("admin:cafe_cook_change", args=[self.cook.id])
        response = self.client.get(url)
        self.assertContains(response, self.cook.years_of_experience)

    def test_cook_add_years_of_experience_listed(self):
        """
        Test that cook's years of experience is on add cook admin page
        """
        url = reverse("admin:cafe_cook_add")
        response = self.client.get(url)
        self.assertContains(response, "First name")
        self.assertContains(response, "Last name")
        self.assertContains(response, "Years of experience")

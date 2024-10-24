from django.contrib.auth import get_user_model
from django.test import TestCase

from cafe.models import DishType, Dish


class ModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="test")
        self.assertEqual(str(dish_type), "test")

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(cook),
            f"{cook.username}"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="test")
        dish = Dish.objects.create(
            name="test", dish_type=dish_type, price=15.9
        )
        self.assertEqual(
            str(dish),
            dish.dish_type.name)

    def test_create_cook_with_years_of_experience(self):
        username = "test"
        password = "test123"
        years_of_experience = 12
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)

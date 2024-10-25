from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from cafe.models import DishType, Dish, Cook

DISH_TYPE_URL = reverse("cafe:dish-type-list")
DISH_URL = reverse("cafe:dish-list")
COOK_URL = reverse("cafe:cook-list")


class PublicDishTypeTests(TestCase):
    def test_login_required(self):
        response = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)


class DishTypesSearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_no_search_query(self):
        DishType.objects.create(name="Soup")
        DishType.objects.create(name="Meat")
        DishType.objects.create(name="Pasta")

        response = self.client.get(DISH_TYPE_URL)

        self.assertEqual(response.status_code, 200)

        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]), list(dish_types)
        )


class PublicDishTests(TestCase):
    def test_login_required(self):
        response = self.client.get(DISH_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

        self.dish_type = DishType.objects.create(name="Soup")

    def test_retrieve_dishes(self):
        Dish.objects.create(
            name="Tomato Soup", dish_type=self.dish_type, price=5.0
        )
        Dish.objects.create(
            name="Chicken Soup", dish_type=self.dish_type, price=5.0
        )

        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)

        dishes = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes),
        )
        self.assertTemplateUsed(response, "cafe/dish_list.html")


class DishSearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

        self.dish_type = DishType.objects.create(name="Soup")

        Dish.objects.create(
            name="Beef Soup", dish_type=self.dish_type, price=5.0
        )
        Dish.objects.create(
            name="Vegetable Soup", dish_type=self.dish_type, price=5.0
        )

    def test_search_dish(self):
        response = self.client.get(DISH_URL, {"name": "Vegetable Soup"})
        self.assertEqual(response.status_code, 200)

        dishes = Dish.objects.filter(name__icontains="Vegetable Soup")

        self.assertEqual(len(response.context["dish_list"]), dishes.count())

    def test_no_search_query(self):
        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)

        dishes = Dish.objects.all()
        self.assertEqual(list(response.context["dish_list"]), list(dishes))


class PublicCookTests(TestCase):
    def test_login_required(self):
        response = self.client.get(COOK_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_create_cooks(self):
        Cook.objects.create(username="cook1", years_of_experience="45")
        Cook.objects.create(username="cook2", years_of_experience="6")

        response = self.client.get(COOK_URL)
        self.assertEqual(response.status_code, 200)

        cooks = Cook.objects.all()
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks),
        )
        self.assertTemplateUsed(response, "cafe/cook_list.html")


class CookSearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_search_cook(self):
        Cook.objects.create(username="cook1", years_of_experience="1")
        Cook.objects.create(username="cook2", years_of_experience="6")
        Cook.objects.create(username="cook3", years_of_experience="34")

        response = self.client.get(COOK_URL, {"username": "cook1"})

        self.assertEqual(response.status_code, 200)
        cooks = Cook.objects.filter(username__icontains="cook1")
        self.assertEqual(list(response.context["cook_list"]), list(cooks))

        self.assertEqual(len(response.context["cook_list"]), 1)

    def test_no_search_query(self):
        Cook.objects.create(username="cook1", years_of_experience="1")
        Cook.objects.create(username="cook2", years_of_experience="6")
        Cook.objects.create(username="cook3", years_of_experience="34")

        response = self.client.get(COOK_URL)

        self.assertEqual(response.status_code, 200)

        cooks = Cook.objects.all()
        self.assertEqual(list(response.context["cook_list"]), list(cooks))

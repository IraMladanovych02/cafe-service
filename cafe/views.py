from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from cafe.models import Dish, DishType, Cook


def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()
    context = {
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks
    }
    return render(request, "cafe/index.html", context=context)
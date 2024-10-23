from django import forms

from cafe.models import Dish, DishType, Cook


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = "__all__"
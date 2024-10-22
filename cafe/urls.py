from django.urls import path

from cafe.views import *

urlpatterns = [
    path("", index, name="index"),
]

app_name = "cafe"

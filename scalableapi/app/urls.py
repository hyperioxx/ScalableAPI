from django.contrib import admin
from django.urls import path

from .views import JsonInputView

urlpatterns = [
    path(
        "input/",
        JsonInputView.as_view(),
        name="inputview",
        ),
]
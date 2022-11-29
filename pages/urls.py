from django.urls import path

from .views import index, addMessage

urlpatterns = [
    path("", index, name="index"),
    path("add/", addMessage, name="add")
]

from django.urls import path

from .views import index, addMessage, messages

urlpatterns = [
    path("", index, name="index"),
    path("add/", addMessage, name="add"),
    path("messages/<int:userid>/", messages, name="messages"),
]

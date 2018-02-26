from django.urls import path
from . import views



urlpatterns = [
    path("personal/", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
]
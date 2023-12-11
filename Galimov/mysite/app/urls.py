from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path("", index),
    path("about", about),
    path("contacts", contacts),
]
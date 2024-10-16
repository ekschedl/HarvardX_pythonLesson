from multiprocessing.managers import view_type

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("katja", views.katja, name="katja"),
    path("david", views.david, name="david"),
]
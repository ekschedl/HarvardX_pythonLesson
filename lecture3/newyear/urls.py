from django.urls import path

from hello.urls import urlpatterns

from . import views


urlpatterns = [
    path("", views.index, name="index")
]
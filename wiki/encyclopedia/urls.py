from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("create/", views.create_entry, name="create_entry"),
    path('delete/<str:title>/', views.delete_entry, name='delete_entry'),

]

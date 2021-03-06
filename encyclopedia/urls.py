from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:entry>/", views.entry, name="entry"),
    path("wiki/search", views.search, name="search"),
    path("wiki/random", views.random_page, name="random"), # edit makes Request URL:	http://127.0.0.1:8000/edit
    path("wiki/new", views.new, name="new"),
    path("wiki/<str:title>/edit", views.edit, name="edit")
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry , name="entry"),
    path("search/", views.search , name="search"),
    path("newPage/", views.NewPage, name="newPage"),
    path("edit/", views.edit, name="edit"),
    path("saveEdited/", views.saveEdited, name="saveEdited"),
    path("randomPage/", views.randomPage, name="randomPage")
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit", views.edit, name="edit"),
    path("api/v1/override", views.override, name="override"),
    path("api/v1/pyexecute", views.pyexecute, name="pyexecute"),
    path("api/v1/gcc", views.gcc, name="gcc"),
    path("api/v1/c", views.c, name="c"),
    path("api/v1/js", views.js, name="js"),
    path("api/v1/filenamechange", views.filenamechange, name="filenamechange"),
]

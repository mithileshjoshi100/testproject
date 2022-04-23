from unicodedata import name
from django.urls import path
from . import views

app_name = "homepage"
urlpatterns = [
     path("", views.index, name="index"),
     path("projects", views.project_list, name="projects")
]
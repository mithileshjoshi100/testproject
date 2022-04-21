from unicodedata import name
from django import views
from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path("", views.index, name='index'), 
    path("<str:name>", views.greet, name='greet'),
    path("saurabh", views.saurabh, name='saurabh')
]
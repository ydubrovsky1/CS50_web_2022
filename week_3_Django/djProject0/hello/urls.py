from django.urls import path

# . means this current directory
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("yana", views.yana, name="yana"),
    path("gaga", views.gaga, name="gaga"),

    #this route could be any string, will call greet function and pass in that string as name
    path("basicgreet:<str:name>", views.greet, name="greet"),

    path("greet:<str:name>", views.greetpg, name="greetpg")
]
from django.urls import path, include

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"), 
    path("wiki/<str:entry>", views.wiki, name="entry"),
    path("wiki", views.wiki_search, name="wiki_search"),
    path("newpg", views.newpg, name="newpg"),
    path("editpg", views.editpg, name="editpg"),
    path("randompg", views.randompg, name="randompg")
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newlisting", views.newlisting, name="newlisting"),
    path("<int:listing_id>", views.listingview, name="listingview"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("comment", views.comment, name="comment"),
    path("bid", views.bid, name="bid"),
    path("close", views.close, name="close"),
    path("categories", views.categories, name="categories"),
    path("Category/<str:category_name>", views.category, name="Category")
]

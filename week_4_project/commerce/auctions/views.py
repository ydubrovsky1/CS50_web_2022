from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import sqlite3

from .models import User, Listing, Comment, Bid

@login_required
def bid(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = Listing.objects.get(id=listing_id)
        price = listing.min_bid
        bid =  float(request.POST["bid"])

        if bid <= price:
            return render(request, "auctions/error.html", {
                "message": "Bid was Less Than Item Price"
            })
        else:    
            current_user = request.user
            bid_obj = Bid(
                listing=listing, 
                user=current_user, 
                amount=bid 
                )
            bid_obj.save()

            listing.min_bid=bid
            listing.winning_user=current_user.username
            listing.save()
    return render(request, "auctions/listing.html",{
        "listing": listing,
        "comments": listing.listing_comment.all()
    })

def categories(request):
    listings = Listing.objects.all()
    categories = ["Electronics","Food","Home","Pets", "Tickets", "Toys", "Other"]
    return render(request, "auctions/categories.html",{
                "listings": listings,
                "categories" : categories
    })

@login_required
def close(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = Listing.objects.get(id=listing_id)
        current_user = request.user
        owner = listing.owner
        if current_user != owner:
            return render(request, "auctions/error.html", {
                "message": "Only the User Who Created This Auction Can Close It."
            })
        else:
            listing.active = False
            listing.save()
            return render(request, "auctions/listing.html",{
                "listing": listing,
                "comments": listing.listing_comment.all()
            })

@login_required
def comment(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = Listing.objects.get(id=listing_id)
        current_user = request.user
        comment_text =  request.POST["comment"]
        comment = Comment(
            listing=listing, 
            user=current_user, 
            comment=comment_text 
            )

        comment.save()
    return render(request, "auctions/listing.html",{
        "listing": listing,
        "comments": listing.listing_comment.all()
    })

@login_required
def watchlist(request):
    current_user = request.user
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = Listing.objects.get(id=listing_id)
        if request.POST["do_what"] == "add": 
            current_user.watchlist.add(listing)
            current_user.save
        if request.POST["do_what"] == "delete": 
            current_user.watchlist.remove(listing)
            current_user.save
    return render(request, "auctions/watchlist.html",{
        "watchlist": current_user.watchlist.all()
    })


def listingview(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.user.is_authenticated == False: 
        return render(request, "auctions/nologin_listing.html",{
        "listing": listing,
        "comments": listing.listing_comment.all(),
    })
    return render(request, "auctions/listing.html",{
        "listing": listing,
        "comments": listing.listing_comment.all(),
        "user": request.user,
    })

def category(request, category_name):
    listings = Listing.objects.all()
    category_listings = []
    for listing in listings:
        if listing.category == category_name:
            category_listings.append(listing)
    return render(request, "auctions/category.html",{
        "category":category_name,
        "listings":category_listings
    })

def index(request):
    return render(request, "auctions/index.html",{
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def newlisting(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        photo_url= request.POST["photo_url"]
        min_bid = request.POST["min_bid"]
        category = request.POST["category"]
        owner = request.user
        
        listing = Listing(
            name=name, 
            description=description, 
            photo_url=photo_url,
            min_bid=min_bid,
            category=category,
            owner=owner,)
        listing.save()

        owner.listings.add(listing)
        owner.save

        return render(request, "auctions/listing.html", {
                "listing":listing
            })
    else:
        return render(request, "auctions/newlisting.html")



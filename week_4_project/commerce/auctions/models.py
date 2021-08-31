from django.contrib.auth.models import AbstractUser
from django.db import models

#a class for auction listings

class User(AbstractUser):
    listings = models.ManyToManyField('Listing', blank=True, related_name="l_user") 
    watchlist = models.ManyToManyField('Listing', blank=True, related_name="w_user")

class Listing(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    photo_url = models.URLField(max_length=200, blank=True)
    min_bid = models.DecimalField(max_digits=8, decimal_places=2, default=10.00)
    winning_user = models.CharField(max_length=20, default="none") 
    CategoryType = (
        ('Electronics', 'Electronics'),
        ('Food', 'Food'),
        ('Home', 'Home'),
        ('Other', 'Other'),
        ('Pets', 'Pets'),
        ('Tickets', 'Tickets'),
        ('Toys', 'Toys'),
    )
    category = models.CharField(blank=True, choices=CategoryType, max_length=15)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="u_listing", default=0) 
    comment = models.ManyToManyField('Comment', blank=True, related_name="c_listing")
 
    def __str__(self):
        return f"{self.name}: {self.description}"


class Bid(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_bid")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bid")     

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment") 
    comment = models.CharField(max_length=120)    

    def __str__(self):
        return f"Comment: {self.comment}, on Listing: {self.listing.name}"





from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from operator import itemgetter

from .models import User, Post

import datetime

@csrf_exempt
@login_required
def follow(request):
    # Requesting to follow must be via post
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    # get user to follow and if follow or unfollow
    data = json.loads(request.body)
    uTF = data.get("userToFollow", "")
    userToFollow = User.objects.get(username=uTF)
    followRequest = data.get("followRequest", "")
    user = request.user
    if followRequest == "follow":
        user.following.add(userToFollow)
        userToFollow.followers.add(user)
    else:
        user.following.remove(userToFollow)
        userToFollow.followers.remove(user)
    user.save()
    userToFollow.save()
    return JsonResponse({"message": "You Are Now following"}, status=201)

@login_required
def following(request):
    uFs = request.user.following.all() 
    posts = []
    for uF in uFs:
        posts1 = Post.objects.filter(author = uF.username)
        posts.extend(posts1)
    orderedPosts = sorted(posts, key=lambda x: x.date) 
    return render(request, "network/index.html",{
        "posts": orderedPosts,
    })

def index(request):
    return render(request, "network/index.html",{
        "posts": Post.objects.all(),
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def newPost(request):
    if request.method =="POST":
        postBody = request.POST["newPost_body"]
        username = request.user.username
        likes = 0
        newPostObj = Post(
            author=username,
            body=postBody,
            likes=likes)
        newPostObj.save()
        return render(request, "network/test.html", {
            "object": newPostObj,
        })

def profile(request, user_name):
    #user doesn't exist
    if(False):
        return render(request, "network/error.html",{
            "error": "user does not exist",
        })
    else:
        profile_user = User.objects.get(username=user_name)
        posts = Post.objects.filter(author=profile_user)
        current_user = request.user
    #check if this is viewers own page
    if profile_user == current_user:
        ownPage = True
    else:
        ownPage = False

    #check if viewer is following the user whose profile is being viewed
    following = False
    if current_user.following.filter(username__contains= profile_user).exists():
        following = True
    
    return render(request, "network/profile.html",{
        "profile_user":profile_user,
        "posts":posts,
        "ownPage": ownPage,
        "following": following,
    })


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

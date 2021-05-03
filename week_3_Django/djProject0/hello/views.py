from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def yana(request):
    return HttpResponse("Yana is bad b.")

def gaga(request):
    return HttpResponse("Paws Up")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def greetpg(request, name):
    return render(request, "hello/greetpg.html", {
        "name": name.capitalize()
    })
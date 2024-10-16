from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, a new world!")

def index(request):
    return render(request,"hello/index.html")

def katja(request):
    return HttpResponse("Hello, Katja!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()} !")
    return render(request,"hello/greet.html",{"name":name.capitalize()})
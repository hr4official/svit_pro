from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "index.html",{})

def contact(request):
    return render(request, "contact.html",{})

def help1(request):
    return render(request, "help.html",{})

def product1(request):
    return render(request, "products.html",{})

def login(request):
    return render(request, "login.html",{})

def signup(request):
    return render(request, "signup.html",{})

    
"""
def index_view(request):
    return HttpResponse("hello") """
    
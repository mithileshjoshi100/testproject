import re
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def saurabh(request):
    return HttpResponse('Hello, Saurabh !!')

def greet(request,name):
    return render(request, "hello/greet.html",{
        "name":name+'56'
    })
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"Teachers/index.html")

def navbar(request):
    return render(request,"Teachers/navbar.html")
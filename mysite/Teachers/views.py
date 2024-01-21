from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"Teachers/index.html")


#delete when the page is ready
def navbar(request):
    return render(request,"Teachers/newAndUpd.html")
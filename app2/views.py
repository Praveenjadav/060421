from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>This is direct html code of app2 </h1>")

def page1(request):
    return render(request,"sample2.html")

def sample_app2(request):
    return render(request,"sample_app2.html")

from django.shortcuts import render
from django.http import HttpResponse
app_name="app1"

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is direct html code of app1 </h1>")

def page1(request):
    return render(request,"sample1.html")

def sample_app1(request):
    return render(request,"sample_app1.html")

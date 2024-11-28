from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def veg(request):
    return HttpResponse('<h1>In meghana retuarent veg biryani also available</h1>')
def paneer(rquest):
    return HttpResponse('<h1>paneer biryani is very tasty</h1>')
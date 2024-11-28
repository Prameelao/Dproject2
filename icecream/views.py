from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def chacolate(request):
    return HttpResponse('<h1>Chacolate icecream is good for health</h1>')
def vennela(request):
    return HttpResponse('<h1>vennela is the one of the famouse brand</h1>')

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def cool(request):
    return HttpResponse('<h1>There is sale for cakes on swiggy</h1>')
def honey(request):
    return HttpResponse('<h1>honey cake is aloso available in swiggi</h1>')
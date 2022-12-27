from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def manish(request):
    return HttpResponse('<h1>hii i am manish </h1>')

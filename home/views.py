from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def base(request):
    return render(request, 'home/base.html')

def simple(request):
    return render(request, 'home/simple.html')


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def company(request):
    return render(request, 'company/company.html')

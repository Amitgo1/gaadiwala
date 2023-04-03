from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactInformation

# Create your views here.

def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(name,email, phone,message)
        if name and email and phone and message:
            ContactInformation.objects.create(name  = name, email = email, phone = phone, message = message)
            # eske baad cmd main ek qurey chalo python manage.py shell
            # fir import karo class from aapname.models import *
            # fir us class ka object banao
    return render(request, 'contactus/contact.html')

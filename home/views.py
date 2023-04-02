from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactDetails

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        Phone = request.POST.get("Phone")
        Message = request.POST.get("Message")
        print(name,email,Phone,Message)
        # insert into ki query
        if name and email and Phone and Message:
            ContactDetails.objects.create(name=name, email=email, Phone=Phone, Message=Message)
        # dekhne ke query
        # queryset = ContactDetails.objects.all()
    queryset = ContactDetails.objects.all()
    data = queryset.values()
    return render(request, 'home/index.html', {"data":data})
    # else:
    #     ContactDetails.objects.create(name=name, email=email, Phone=Phone, Message=Message)
    #     return render(request, 'home/index.html')
        

def base(request):
    return render(request, 'home/base.html')


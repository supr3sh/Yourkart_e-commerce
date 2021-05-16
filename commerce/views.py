from django.shortcuts import render 
from django.http import HttpResponse 
from shop.models import Contact

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        query = request.POST.get('query', '')
        
        contact = Contact(name=name, email=email, phone=phone, query=query)
        contact.save()
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
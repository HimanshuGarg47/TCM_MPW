from django.shortcuts import render 
from django.http import HttpResponse
from django.template import loader
from .models import Enquiry
# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST["Name"]
        email = request.POST["Email"]
        number = request.POST["PNumber"]
        message = request.POST['message']
        enquiry = Enquiry(name = name , email_address = email , phone = number, content = message)
        enquiry.save()
        return render(request, 'Home/Success_Query.html' , {})
    return render(request,'Home/index.html');

def alumni(request):
    return render(request,'Home/alumni.html' ,{})

def team(request):
    return render(request, "Home/team.html", {})

def Event(request):
    return render(request , "Home/events.html")





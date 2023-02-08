from django.dispatch import receiver
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from .models import Enquiry
# from django.contrib.sites.models import Site


from  mysite.settings import *
# from django.conf import settings
# from ..mysite import settings

from twilio.rest import Client

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST["Name"]
        email = request.POST["Email"]
        number = request.POST["PNumber"]
        message = request.POST['message']
        enquiry = Enquiry(name = name , email_address = email , phone = number, content = message)
        enquiry.save()
        broadcast_sms(request , number)
        # return redirect('/broadcast')
        # return render(request, 'Home/Success_Query.html' , {})
    return render(request,'Home/index.html');


def broadcast_sms(request , recipient):
    # current_site = Site.objects.get_current()
    
    message_to_broadcast = ("We have received your request for enquiry."
                                                f'We will inform you status about your enquiry by email.')
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    # for recipient in SMS_BROADCAST_TO_NUMBERS:
    #     if recipient:
    print(type(recipient))
    print(recipient)
    print(str(recipient))
    client.messages.create(to=str(recipient),from_= TWILIO_NUMBER,body=message_to_broadcast)
    # return HttpResponse("messages sent!", 200)


def alumni(request):
    return render(request,'Home/alumni.html' ,{})

def team(request):
    return render(request, "Home/team.html", {})

def Event(request):
    return render(request , "Home/events.html")

def quiz(request):
    return HttpResponse("quiz", 200)

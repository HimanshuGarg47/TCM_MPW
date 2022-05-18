from base64 import urlsafe_b64decode
from email.message import EmailMessage
from lib2to3.pgen2.tokenize import generate_tokens
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout , login as auth_login
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from mysite import settings
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes , force_str
from . tokens import generate_token as gen_token
# Create your views here.

def home(request):
    return render(request,"Home/index.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]
        
        user = authenticate(username=username , password = pass1)
        if user is not None:
            auth_login(request ,user)
            fname = user.first_name
            messages.success(request, "Logged In successfully")
            return render(request, "Home/index.html", {"fname":fname,})
        
        else:
            messages.error(request, "Bad credentials")
            return redirect('/User/login/')
        
    return render(request,"Authentication/login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]   
        
        if not username.isalnum():
            messages.error(request , "Username must be Alpha-Numeric")
            return redirect('/User/signup')
        
        if User.objects.filter(username = username):
            messages.error(request , "Username already exist. Please try with other username")
            return redirect('/User/signup')
        
        if User.objects.filter(email = email):
            messages.error(request , "Email already exist. Please try with other Email")
            return redirect('/User/signup')
        
        if pass1 != pass2:
            messages.error(request , "Both passwords should match")
            return redirect('/User/signup')
        
        
        myuser = User.objects.create_user(username , email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save() 
        
        messages.success(request, "Your account has been created successfully. We have also sent you a confirmation email. Please confirm your email in order to activate your account. ")
        
        
        # welcome Email
        
        subject = "Welcome to CodingTalks community"
        message = "Hello " + myuser.first_name + "!!\n" + "Welcome to CodingTalks!!\n" + "Thanku for visiting our website \n" + "We have also sent you a confirmation email.\n Please confirm your email in order to activate your account. \n\n Thanking Your Himanshu Garg"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject , message , from_email , to_list , fail_silently = True)
        
        # Email Address Confirmation email
        
        current_site = get_current_site(request)
        email_subject = "Confirm your email @CodingTalks - Django Login!!"  
        message2 = render_to_string('email_confirmation.html', {
            'name':myuser.first_name + myuser.last_name,
            'domain':current_site.domain,
             'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
             'token':gen_token.make_token(myuser)
             
        } )
        email = EmailMessage(email_subject , message2, settings.EMAIL_HOST_USER, [myuser.email])
        email.fail_silently = True
        email.send()
        return redirect('/User/login')
        
    return render(request,"Authentication/signup.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('/')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError , ValueError , OverflowError,User.DoesNotExist):
        user = None
    if user is not None and gen_token.check_token(user,token):
        user.is_active = True
        user.save()
        auth_login(request , user)
        return redirect('home')
    else:
        return render(request, 'Authentication/activation_failed.html')

         
         
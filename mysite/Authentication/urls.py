from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home , name="home"),
    path("login/" , views.login, name="login"),
    path("signup/", views.signup , name="signup"),
    path("signout/", views.signout , name="signout"),
    path("activate/<uidb64>/<token>/", views.activate , name="activate"),


    
    
] 
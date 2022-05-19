from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alumni/', views.alumni , name='alumni'),
    path('team/', views.team , name="team"),
    path('events/', views.Event , name="event"),

]
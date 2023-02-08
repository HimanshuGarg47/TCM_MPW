from django.urls import path , re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alumni/', views.alumni , name='alumni'),
    path('team/', views.team , name="team"),
    path('events/', views.Event , name="event"),
    path('quiz/', views.quiz , name="quiz"),

    re_path(r'broadcast$', views.broadcast_sms, name="default"),
    

]
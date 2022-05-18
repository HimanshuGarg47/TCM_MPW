from django.urls import path

from .views import HomeView , ArticleDetailView

urlpatterns = [
    # path('', views.blog, name='blog'),
    path('',HomeView.as_view(), name="blog_home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = "detailpost")
    
]
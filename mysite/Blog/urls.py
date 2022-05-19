from django.urls import path

from .views import HomeView , ArticleDetailView, AddPostView, UpdatePostView , DeletePostView

urlpatterns = [
    # path('', views.blog, name='blog'),
    path('',HomeView.as_view(), name="blog_home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = "detailpost"),
    path('add_post/', AddPostView.as_view() , name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = "updatepost"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name = "deletepost"),


    
    
]
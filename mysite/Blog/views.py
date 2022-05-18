from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post
# Create your views here.
# def blog(request):
#     pass

class HomeView(ListView):
    model = Post
    template_name = 'Blog/home.html'
    
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Blog/article_detail.html'
    
    
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Post
from .forms import PostForm , EditForm 
# Create your views here.
# def blog(request):
#     pass

class HomeView(ListView):
    model = Post
    template_name = 'Blog/home.html'
    ordering = ['-id']
    
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Blog/article_detail.html'
    
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Blog/add_post.html'
    # fields = '__all__'
    
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm 
    template_name = 'Blog/update_post.html'
    # fields = ['title' , 'title_tag', 'body']
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'Blog/delete_post.html'
    success_url = reverse_lazy('blog_home')
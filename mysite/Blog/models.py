from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=50)
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title + " | " + str(self.author)
    
    def get_absolute_url(self):
        return reverse('blog_home')
        # return reverse("detailpost", args=(str(self.id)))
    
    
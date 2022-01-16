from re import template
from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView,CreateView

# Create your views here.
def frontpage(request):
    
    
    posts=Post.objects.all()
    return render(request,'frontpage.html',{'posts':posts})

class DetailView(DetailView):
    model = Post
    template_name = "articles.html"

class AddPostView(CreateView):
    model=Post
    template_name = "add_post.html"
    fields = '__all__'

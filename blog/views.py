from django.shortcuts import redirect, render
from django.contrib import messages
from .models import BlogPost
# Create your views here



def home(request):    
    blogPosts =BlogPost.objects.all()
    conext= {'blogPosts':blogPosts}
    return render(request,'blog/home.html', conext)


def blogPosts(request,pk):    
    blogStory =BlogPost.objects.get(id=pk)
    css_class = 'animate-box'
    context= {'blogStory':blogStory,'css_class':css_class}
    return render(request,'blog/blog_post.html',context, )
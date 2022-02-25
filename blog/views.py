from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models  import BlogPost
from .forms import NewUserForm
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

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')
    context = { 'page' :'login'}
    return render(request,'blog/login.html',context)

def registerPage(request):
    form = NewUserForm()
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    context = {'form': form,'page':'Register'}
    return render(request, 'blog/login.html', context )
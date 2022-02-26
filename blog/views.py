from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import BlogPostForm ,NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models  import BlogPost
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


def createUpdateBlog(request):
    form = BlogPostForm()
    if request.method == 'POST': 
        BlogPost.objects.create(
            blogTitle = request.POST.get('blogtitle'),
            description = request.POST.get('description'),
            story = request.POST.get('story'),
         )
        return redirect('home')
    context = {'form':form}
    return render(request,'blog/create_update_blog.html',context)

@login_required(login_url='login')  
def deleteBlog(request,pk):
    blog = BlogPost.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
    return redirect('home')

 
def loginPage(request):
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

def logoutUser(request):
    logout(request)
    return redirect('home')

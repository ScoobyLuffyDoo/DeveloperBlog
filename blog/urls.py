from django.urls import path
from . import views


urlpatterns = [
 path('',views.home, name="home"),
 path('blog-post/<str:pk>',views.blogPosts, name="blog-post"),
 path('login/',views.login, name="login"),
 path('register/',views.registerPage, name="register"),
 
]
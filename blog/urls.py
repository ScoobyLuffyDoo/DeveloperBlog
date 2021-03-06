from django.urls import path
from . import views

urlpatterns = [
 path('',views.home, name="home"),
 path('myProfile/<username>/',views.myProfile, name="myProfile"),
 path('blog-post/<str:pk>',views.blogPosts, name="blog-post"),
 path('create_update_blog',views.createBlog, name="create_update_blog"),
 path('update_blog/<str:pk>',views.updateBlog, name="update_blog"),
 path('delete_blog/<str:pk>',views.deleteBlog, name="delete_blog"), 
 path('login/',views.loginPage, name="login"),
 path('register/',views.registerPage, name="register"),
 path('logout/',views.logoutUser, name="logout"),
 
]
from pyexpat import model
from django.forms import ModelForm
from .models import BlogPost


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields ='__all__'
        exclude = ['-created', '-updated']

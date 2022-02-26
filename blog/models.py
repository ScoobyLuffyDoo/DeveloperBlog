from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class BlogPost(models.Model):
    blogTitle = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True, blank=True, max_length=300)
    story = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return (self.blogTitle)
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from ckeditor.fields import RichTextField




# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    

class Postdata(models.Model):
    title = models.CharField(max_length=255)

    header_image = models.ImageField(blank=True, null=True, upload_to='images/') # This was added to hold imaages

    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank = True, null = True)
    #body = models.RichTextField()
    published_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_like(self):
        return self.likes.count()

    def __str__(self):
        return self.title +  ' | '  + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

# This is used to add bio to our profile
class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(blank=True, null=True, upload_to='images/')
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user)

class Comment(models.Model):
    post = models.ForeignKey(Postdata, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    date_made = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


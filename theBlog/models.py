# from turtle import title
# from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('theBlog:article_detail',  kwargs={'pk':self.pk})
        return reverse('theBlog:home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(default="")
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=255, default="Click link above to read blog post..")
    # body = models.TextField(default="")
    # on_DELETE to delete the posts too after author is gone
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    category = models.CharField(max_length=225, default='uncategorised')
    likes = models.ManyToManyField(User, related_name='blog_posts')


    def __str__(self):
        return self.title + ' |' + str(self.author)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        # return reverse('theBlog:article_detail',  kwargs={'pk':self.pk})
        return reverse('theBlog:home')

class Comment(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        # return '%s - %s' % (self.post.title, self.name)
        return f"By: {self.user}, on: {self.post.author.username}'s {self.post.title} post."



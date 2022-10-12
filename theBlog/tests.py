from django.test import TestCase, Client

from django.contrib.auth.models import User
from .models import Category, Comment, Profile, Post
# Create your tests here.

class PostTestCase(TestCase):

    def setUp(self):
        user1 = User.objects.create(username='default', password='password',
        email='default@email.com')
        user2 = User.objects.create(username='default1', password='password1',
        email='default2@email.com')
        profile1 = Profile.objects.create(user=user1)
        post1 = Post.objects.create(title='test title', author=user1, body='this is a test body')
        post2 = Post.objects.create(title='test title two', author=user2, body='this is ser2 test body')
        
    def post_like_count(self):
        post1 = Post.objects.get(title='test title')
        user1 = User.objects.get(username='default')
        user2 = User.objects.get(username='default1')
        post1.likes.add(user2)
        post1.likes.add(user1)
        self.assertEqual(post1.likes.count(), 2)

    def post_comment_count(self):
        post1 = Post.objects.get(title='test title')
        user2 = User.objects.get(username='default2')
        comment1 = Comment.objects.create(user=user2, post=post1, content='test content')
        self.assertEqual(Comment.objects.filter(post=post1).count(), 1)

    def unlike_post(self):
        post1 = Post.objects.get(title='test title')
        user2 = User.objects.get(username='default2')
        post1.likes.remove(user2)
        self.assertEqual(post1.likes.count(), 1)

    def test_home(self):

        c = Client()
        response = c.get("")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object_list'].count(), 2)

    def test_blog(self):
        p = Post.objects.get(title='test title')
        c = Client()
        response = c.get(f"/article/{p.id}")
        self.assertEqual(response.status_code, 200)
        
from django.test import TestCase
from .models import Post

from django.contrib.auth.models import User
from django.test.client import Client



class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='myuser')
        self.post = Post.objects.create(title="My title",text="abc",created_date="1990-01-01", author=self.user)


    def test_post(self):
        self.assertEqual(self.post.title, "My title")
        self.assertEqual(self.post.text, "abc")
        self.assertEqual(self.post.created_date, "1990-01-01")
        self.assertEqual(self.post.author.username, "myuser")


    # def test_post_title(self):
    #     post = Post(title="My title")
    #     post = Post(text ="my text")
    #     self.assertEqual(str(post), post.title)
    #     self.assertEqual("my text", post.text)


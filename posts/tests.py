from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
         testuser_1 = User.objects.create_user(
             username='amir', password='1234'
         )
         testuser_1.save()
         testpost_1 = Post.objects.create(
             author=testuser_1 , title='django' , body='django ...'
         )
         testpost_1.save()
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.author.username, 'amir')
        self.assertEqual(post.title, 'django')
        self.assertEqual(post.body, 'django ...')

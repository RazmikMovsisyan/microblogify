from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass')
        self.post = Post.objects.create(title='Test Title', slug='test-title', content='Test Content', author=self.user)

    def test_post_str_method(self):
        self.assertEqual(str(self.post), 'Test Title')

    def test_post_content(self):
        self.assertEqual(self.post.content, 'Test Content')
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class PostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass')
        self.post = Post.objects.create(title='View Title', slug='view-title', content='View Content', author=self.user)
        self.client.login(username='tester', password='pass')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Title')
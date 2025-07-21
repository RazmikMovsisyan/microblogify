from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostListView

class TestUrls(SimpleTestCase):
    def test_post_list_url_resolves(self):
        url = reverse('post_list')
        self.assertEqual(resolve(url).func.view_class, PostListView)
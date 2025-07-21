from django.test import TestCase
from blog.forms import CommentForm

class CommentFormTest(TestCase):
    def test_valid_comment(self):
        form = CommentForm(data={'content': 'Nice post!'})
        self.assertTrue(form.is_valid())

    def test_too_long_comment(self):
        form = CommentForm(data={'content': 'x' * 1001})
        self.assertFalse(form.is_valid())
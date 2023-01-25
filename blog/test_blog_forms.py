from django.test import TestCase
from ..forms import PostForm

class PostFormTest(TestCase):

    def test_fields_form_class(self):
        post = PostForm()
        self.assertEqual(post.Meta.fields, ['title', 'content',])
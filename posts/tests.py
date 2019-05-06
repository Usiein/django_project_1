from django.test import TestCase
from .models import Post
# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')
        Post.objects.create(text='another test issue')

    def test_text_content(self):
        post = Post.objects.get(id=2)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'another test issue')

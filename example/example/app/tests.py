from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from app.models import Post


class TestPage(TestCase):

    def setUp(self):
        self.client = Client()
        Post.objects.create(text='# Header')

    def test_index_page(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, '<h1>Header</h1>')

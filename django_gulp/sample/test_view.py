from __future__ import unicode_literals
from django.test import TestCase
from django.urls import reverse

class SampleViewTest(TestCase):

    fixtures = ['initial_data.yaml']

    def setUp(self):
        pass

    def test_detail(self):
        response = self.client.get(reverse('sample:detail'))
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertInHTML('<li>1 お仕事1</li>', content)

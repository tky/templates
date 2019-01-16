from __future__ import unicode_literals
from django.test import TestCase
from . import models

class TaskTestCase(TestCase):

    fixtures = ['initial_data.yaml']

    def setUp(self):
        pass

    def test_find_task(self):
        task = models.Task.objects.get(pk=1)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.name, "お仕事1")

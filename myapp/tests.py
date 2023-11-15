from django.test import TestCase
from .models import MyModel

class MyModelTests(TestCase):
    def test_database(self):
        count_before = MyModel.objects.count()

        # Create a new record
        MyModel.objects.create(name='Test Name', description='Test Description')

        count_after = MyModel.objects.count()
        self.assertEqual(count_after, count_before + 1)

from django.test import TestCase

class InitialTest2(TestCase):
    """Initial tests"""
    def test_two(self):
        self.assertEqual(2*2, 4)

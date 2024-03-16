from django.test import TestCase

class DummyTestCase(TestCase):
    def test_dummy_1(self):
        self.assertEqual(1 + 1, 2)

    def test_dummy_2(self):
        self.assertTrue(True)
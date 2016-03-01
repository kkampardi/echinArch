from django.test import TestCase

# Create your tests here.
class portfolioTest(TestCase):
    def test_index(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)

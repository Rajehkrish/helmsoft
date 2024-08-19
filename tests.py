import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_ip(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('ip', response.get_json())

if __name__ == '__main__':
    unittest.main()

# test_app.py

import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

    def test_about_page(self):
        response = self.app.get('/#about')
        self.assertEqual(response.status_code, 200)

    def test_products_page(self):
        response = self.app.get('/#products')
        self.assertEqual(response.status_code, 200)


    def test_contact_page(self):
        response = self.app.get('/#contact')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

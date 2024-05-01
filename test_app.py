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
        # Adjust the assertion to check for the expected HTML content related to your chocolate shop
        self.assertIn('<title>Chocolate Shop</title>', response.data.decode('utf-8'))

    def test_about_page(self):
        response = self.app.get('/#about')
        self.assertEqual(response.status_code, 200)
        # Add more assertions if needed for the about page
        # Example:
        # self.assertIn('About Us', response.data.decode('utf-8'))

    def test_products_page(self):
        response = self.app.get('/#products')
        self.assertEqual(response.status_code, 200)
        # Add more assertions if needed for the products page
        # Example:
        # self.assertIn('Our Chocolate Products', response.data.decode('utf-8'))

    def test_contact_page(self):
        response = self.app.get('/#contact')
        self.assertEqual(response.status_code, 200)
        # Add more assertions if needed for the contact page
        # Example:
        # self.assertIn('Contact Us', response.data.decode('utf-8'))
        # self.assertIn('Phone', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()

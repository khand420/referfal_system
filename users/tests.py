# users/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserViewsTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(email='test@example.com', name='Test User', password='testpassword')

    def test_register_user(self):
        url = reverse('register_user')
        data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'password': 'newuserpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('user_id', response.data)
        self.assertEqual(response.data['message'], 'User registered successfully')

    def test_user_details(self):
        url = reverse('user_details')
        # Use the test user's token for authentication
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.user.name)
        self.assertEqual(response.data['email'], self.user.email)

    def test_referrals(self):
        url = reverse('referrals')
        # Use the test user's token for authentication
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions based on expected response data for referrals

        # Clean up: delete the test user after testing
        self.user.delete()

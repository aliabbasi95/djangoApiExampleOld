from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class AccountsTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user.
        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')

        # URL for creating an account.
        self.register_url = reverse('account_register')

    def test_register_user(self):
        """
        Ensure we can create a new user.
        """
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'Somepassword1@'
        }

        response = self.client.post(self.register_url, data, format='json')

        # We want to make sure we have two users in the database..
        self.assertEqual(User.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        # We want to make sure password is not in response
        self.assertFalse('password' in response.data)

    def test_register_user_with_short_password(self):
        """
        Ensure user is not created for password lengths less than 12.
        """
        data = {
            'username': 'foobar',
            'email': 'foobarbaz@example.com',
            'password': 'f@2F'
        }

        response = self.client.post(self.register_url, data, format='json')
        # We want to make sure we have one user in the database..
        self.assertEqual(User.objects.count(), 1)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # And check length of password in response data equal 1
        self.assertEqual(len(response.data['password']), 1)

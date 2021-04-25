from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountsTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user.
        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')

        # URL for creating an account.
        self.register_url = reverse('account_register')

    def test_register_user(self):  # new
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'Somepassword1@'
        }  # new

        response = self.client.post(self.register_url, data, format='json')  # new

        # We want to make sure we have two users in the database..
        self.assertEqual(User.objects.count(), 2)  # new
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # new
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['username'], data['username'])  # new
        # self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)  # new

import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class EndPointTesting(APITestCase):
    def test_endpoint(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('inputview')
        data = {'A': 1, 'B': 1, 'C': 1}
        correctresponse = {'C': 1, 'B': 1, 'A': 1}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, correctresponse)
        
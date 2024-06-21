from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

class CustomerAPITestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'John_doe',
            'email': 'john@doe.com',
            'password': 'password_mocktest'
        }
        self.customer_data = {
            'user': self.user_data,
            'name': 'John Doe',
        }
        self.url = reverse('customers:CustomerViewSet-list')

    def test_create_customer(self):
        self.customer_data['cpf'] = '19318528043'
        self.customer_data['phone'] = '84992213131'
        response = self.client.post(self.url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

    def test_create_customer_invalid_cpf(self):
        self.customer_data['cpf'] = '1111111110'
        self.customer_data['phone'] = '84992213131'
        response = self.client.post(self.url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())
    
    def test_create_customer_invalid_phone(self):
        self.customer_data['cpf'] = '19318528043'
        self.customer_data['phone'] = '813131'
        response = self.client.post(self.url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())
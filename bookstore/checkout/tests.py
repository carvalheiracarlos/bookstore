from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from model_bakery import baker
from datetime import datetime

from checkout.models import Order

User = get_user_model()

QUANTITY = 5

class OrderAPITestCase(APITestCase):
    def setUp(self):
        self.author = baker.make('books.BookAuthor')
        self.category = baker.make('books.BookCategory')
        self.book = baker.make('books.Book', author=self.author, category=self.category, quantity=QUANTITY)
        self.user = baker.make('authentication.AuthUser')
        self.customer = baker.make('customers.Customer', user=self.user)
        self.admin_user = User.objects.create_superuser(username='admin_user_test', password='admin_user_password')
        self.status = Order.Status

        self.order_data = {
            'book': self.book.id,
            'quantity': QUANTITY 
        }

        self.url = reverse('checkout:OrderViewSet-list')

    def test_create_order(self):
        self.client.force_login(user=self.user, backend=None)
        response = self.client.post(self.url, self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()['status'], self.status.CONFIRMED.label)

    def test_create_order_rejected(self):
        self.order_data['quantity'] += 1
        self.client.force_login(user=self.user, backend=None)
        response = self.client.post(self.url, self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(response.json()['status'], self.status.REJECTED.label)

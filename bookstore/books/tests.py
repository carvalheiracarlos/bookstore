from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from model_bakery import baker
from datetime import datetime

User = get_user_model()
RELEASE_YEAR = 1992
DEFAULT_BOOK_QUANTITY = 10

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.author = baker.make('books.BookAuthor')
        self.category = baker.make('books.BookCategory')
        self.user = baker.make('authentication.AuthUser')
        self.admin_user = User.objects.create_superuser(username='admin_user_test', password='admin_user_password')

        self.book_data = {
            'title': 'random_book',
            'release_year': RELEASE_YEAR,
            'quantity': DEFAULT_BOOK_QUANTITY,
            'author': self.author.id,
            'category': self.category.id,
        }

        self.url = reverse('books:BookViewSet-list')

    def test_create_book(self):
        self.client.force_login(user=self.admin_user, backend=None)
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

    def test_create_book_invalid_year(self):
        self.client.force_login(user=self.admin_user, backend=None)

        self.book_data['release_year'] = -1
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())

        self.book_data['release_year'] = datetime.now().year + 1 
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())

    def test_list_book(self):
        self.client.force_login(user=self.user, backend=None)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_retrieve_book(self):
        book = baker.make('books.Book')
        url_detail = reverse('books:BookViewSet-detail', args=[book.pk])
        self.client.force_login(user=self.user, backend=None)
        response = self.client.get(url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_update_book(self):
        book = baker.make('books.Book', quantity=DEFAULT_BOOK_QUANTITY)
        update_data = {
            'quantity': DEFAULT_BOOK_QUANTITY + 1
        }
        url_detail = reverse('books:BookViewSet-detail', args=[book.pk])
        self.client.force_login(user=self.admin_user, backend=None)
        response = self.client.patch(url_detail, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertEqual(response.json()['quantity'], DEFAULT_BOOK_QUANTITY + 1)

    def test_delete_book(self):
        book = baker.make('books.Book')
        url_detail = reverse('books:BookViewSet-detail', args=[book.pk])
        self.client.force_login(user=self.admin_user, backend=None)
        response = self.client.delete(url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class BookCategoryAPITestCase(APITestCase):
    def setUp(self):
        self.user = baker.make('authentication.AuthUser')
        self.admin_user = User.objects.create_superuser(username='admin_user_test', password='admin_user_password')

        self.book_data = {
            'name': 'random_category',
        }

        self.url = reverse('books:BookCategoryViewSet-list')

    def test_create_book_category(self):
        self.client.force_login(user=self.admin_user, backend=None)
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

    def test_list_book_category(self):
        self.client.force_login(user=self.user, backend=None)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_retrieve_book_category(self):
        book_category = baker.make('books.BookCategory')
        url_detail = reverse('books:BookCategoryViewSet-detail', args=[book_category.pk])
        self.client.force_login(user=self.user, backend=None)
        response = self.client.get(url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

class BookAuthorAPITestCase(APITestCase):
    def setUp(self):
        self.user = baker.make('authentication.AuthUser')
        self.admin_user = User.objects.create_superuser(username='admin_user_test', password='admin_user_password')

        self.book_data = {
            'name': 'random_author',
        }

        self.url = reverse('books:BookAuthorViewSet-list')

    def test_create_book_author(self):
        self.client.force_login(user=self.admin_user, backend=None)
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

    def test_list_book_author(self):
        self.client.force_login(user=self.user, backend=None)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_retrieve_book_author(self):
        book_author = baker.make('books.BookAuthor')
        url_detail = reverse('books:BookAuthorViewSet-detail', args=[book_author.pk])
        self.client.force_login(user=self.user, backend=None)
        response = self.client.get(url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())


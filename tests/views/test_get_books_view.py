from unittest import mock
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from thelibrary.infrastructure.django.models import Book, Author, Category


class GetBooksViewTest(TestCase):

    def setUp(self) -> None:
        self.endpoint = '/library/books/'
        self.client = APIClient()

    # @classmethod
    # def setUpTestData(cls):
        # cls.book = cls._create_data()
        
    def _get(self, data={}):
        return self.client.get(self.endpoint, data=data)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/library/books/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('books_view'))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(reverse('books_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')
        
    # @classmethod
    # def _create_data(cls):
    #     return mock.create_autospec(Book, spec_set=True)

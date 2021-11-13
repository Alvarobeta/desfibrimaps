from unittest import mock
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from unittest import mock
from thelibrary.context.library.domain.book import book_repository
from thelibrary.infrastructure.django.models import Book, Author, Category
from thelibrary.context.library.domain.book.book_repository import BookRepository
from thelibrary.context.library.application.get_books.get_book_handler import GetBookHandler


class TestGetBookHandler(TestCase):

    def setUp(self) -> None:
        self.book_repository = mock.create_autospec(BookRepository, spec_set=True)
        self.handler = GetBookHandler(book_repository=self.book_repository)

    def test_get_book_returned(self):

        book = mock.Mock()
        self.book_repository.find_one_by_id.return_value = book
        response = self.handler(book.id)

        self.book_repository.find_one_by_id.assert_called_with(book_id=book.id)
        self.assertEqual(response, book)

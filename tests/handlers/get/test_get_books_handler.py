from unittest import mock
from django.test import TestCase
from rest_framework import status
from thelibrary.context.library.domain.book.book_repository import BookRepository
from thelibrary.context.library.application.get_books.get_books_handler import GetBooksHandler


class TestGetBooksHandler(TestCase):

    def setUp(self) -> None:
        self.book_repository = mock.create_autospec(BookRepository, spec_set=True)
        self.handler = GetBooksHandler(book_repository=self.book_repository)

    def test_get_book_returned(self):
        books = self.book_repository.find_books.return_value
        response = self.handler()
        self.book_repository.find_books.assert_called()

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.data['books'], books)

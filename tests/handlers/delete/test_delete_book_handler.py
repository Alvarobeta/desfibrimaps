from unittest import mock
from django.test import TestCase
from thelibrary.infrastructure.django.models import Book, Author, Category
from thelibrary.context.library.domain.book import BookRepository
from thelibrary.context.library.application.delete_book.delete_book_handler import DeleteBookHandler


class TestDeleteBookHandler(TestCase):

    def setUp(self) -> None:
        self.book_repository = mock.create_autospec(BookRepository, spec_set=True)
        self.handler = DeleteBookHandler(
            book_repository=self.book_repository
        )

        self.book = self._create_data()

    def test_delete_book(self):
        book = self.book_repository.find_one_by_id.return_value = self.book
        self.handler(self.book.id)

        self.book_repository.find_one_by_id.assert_called_once_with(book_id=book.id)
        self.book_repository.delete.assert_called_once_with(
            book=book
        )

    @classmethod
    def _create_data(cls):
        book = Book.objects.create(
            id='11',
            isbn='123456789',
            title="Book title test",
            author=Author.objects.all().first(),
            description='book mock description',
        )
        book.categories.set(Category.objects.all())

        return book

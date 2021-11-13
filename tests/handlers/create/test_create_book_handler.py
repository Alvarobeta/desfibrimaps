from unittest import mock
from django.test import TestCase
from django.urls import reverse
from thelibrary.infrastructure.django.models import Author, Category
from thelibrary.context.library.domain.author import AuthorRepository
from thelibrary.context.library.domain.book import BookRepository
from thelibrary.context.library.domain.category import CategoryRepository
from thelibrary.context.library.application.create_book.create_book_handler import CreateBookHandler


class TestCreateBookHandler(TestCase):

    def setUp(self) -> None:
        self.book_repository = mock.create_autospec(BookRepository, spec_set=True)
        self.author_repository = mock.create_autospec(AuthorRepository, spec_set=True)
        self.category_repository = mock.create_autospec(CategoryRepository, spec_set=True)
        self.handler = CreateBookHandler(
            author_repository=self.author_repository,
            book_repository=self.book_repository,
            category_repository=self.category_repository
        )

        self.book, self.author, self.category = self._create_data()
        self.category_ids = self.book['categories']

    def test_create_book(self):
        author = self.author_repository.find_one_by_id.return_value = self.author
        categories = self.category_repository.find_categories_by_ids.return_value = self.category
        created_book = self.book_repository.create.return_value

        response = self.handler(self.book)

        self.author_repository.find_one_by_id.assert_called_once_with(author_id=author.id)
        self.category_repository.find_categories_by_ids.assert_called_once_with(category_ids=self.category_ids)
        self.book_repository.create.assert_called_once_with(
            book=self.book, 
            author=author, 
            categories=categories
        )

        self.assertEqual(response.data['book'], created_book)


    def _get_url(self) -> str:
        return reverse('book_create')

    @classmethod
    def _create_data(cls):
        author = Author.objects.create(
            id='11',
            full_name="Alvaro M",
            pseudonym='Beta',
            born='1991-09-18',
            died=None
        )

        category = Category.objects.create(
            id='22',
            name="Fantasy",
            description="category mock description"
        )

        book = {
            'isbn': '1234567', 
            'title':'The Lord Of The Rings', 
            'author': '11', 
            'categories': '22', 
            'description': 'Why they did not use the eagles since the beginning?'
        }

        return book, author, category

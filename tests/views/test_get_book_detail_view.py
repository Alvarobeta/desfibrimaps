from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from thelibrary.infrastructure.django.models import Book, Author, Category


class GetBookDetailViewTest(TestCase):

    def setUp(self) -> None:
        self.endpoint = '/library/book/{book_id}'
        self.client = APIClient()
        self.book = self._create_data()
        
    def _get(self, data={}):
        return self.client.get(self.endpoint, data=data)

    def test_get_detail_ok(self):
        response = self.client.get(self.endpoint.format(book_id=self.book.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)        

    @classmethod
    def _create_data(cls):
        author = Author.objects.create(
            full_name="Alvaro M",
            pseudonym='Beta',
            born='1991-09-18',
            died=None
        )

        category = Category.objects.create(
            name="Fantasy",
            description="category mock description"
        )

        book = Book.objects.create(
            isbn='123456789',
            title="Book title test",
            author=author,
            description='book mock description',
        )
        book.categories.set([category])

        return book

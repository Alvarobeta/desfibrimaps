from django.test import TestCase
from thelibrary.infrastructure.django.models import Book, Author, Category


class GetBooksViewTest(TestCase):

    fixtures = [
        'permissions',
        'locations'
    ]

    @classmethod
    def setUpTestData(cls):
        cls.book = cls._create_data()

    def _get(self, token=None, data={}):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        return self.client.get(self.endpoint, data=data)

    def _assert_contract(self, res):
        data = res.data
        self.assertIn('count', data)
        self.assertIn('next', data)
        self.assertIn('previous', data)
        self.assertIn('results', data)

        self.assertIsInstance(data['count'], int)
        if data['next']:
            self.assertIsInstance(data['next'], str)
        if data['previous']:
            self.assertIsInstance(data['previous'], str)
        self.assertIsInstance(data['results'], list)

        book = res.data['results'][0]
        self.assertIn('id', book)
        self.assertIn('isbn', book)
        self.assertIn('title', book)
        self.assertIn('description', book)
        self.assertIn('author', book)
        self.assertIn('categories', book)

        self.assertIsInstance(book['id'], int)
        self.assertIsInstance(book['isbn'], str)
        self.assertIsInstance(book['title'], str)
        self.assertIsInstance(book['description'], str)
        self.assertIsInstance(book['author'], Author)
        self.assertIsInstance(book['categories'], Category)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/library/books/')
        self.assertEqual(response.status_code, 200)

    @classmethod
    def _create_data(cls):

        author = Author.objects.create(
            id=1,
            full_name="Alvaro M",
            pseudonym='Beta',
            born='1991-09-18'
        )

        category = Category.objects.create(
            id=1,
            name="Fantasy",
            description="category mock description"
        )

        book = Book.objects.create(
            id=1,
            isbn='123456789',
            title="Book title test",
            author=author,
            categories=category,
            description='book mock description'
        )

        return book

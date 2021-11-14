from unittest import mock
from django.test import TestCase
from rest_framework import status
from thelibrary.context.library.domain.author.author_repository import AuthorRepository
from thelibrary.context.library.application.get_authors.get_author_handler import GetAuthorHandler


class TestGetAuthorHandler(TestCase):

    def setUp(self) -> None:
        self.author_repository = mock.create_autospec(AuthorRepository, spec_set=True)
        self.handler = GetAuthorHandler(
            author_repository=self.author_repository
        )

    def test_get_author_returned(self):
        author = self.author_repository.find_one_by_id.return_value
        response = self.handler(author.id)

        self.author_repository.find_one_by_id.assert_called_with(author_id=author.id)
        
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.data['author'], author)

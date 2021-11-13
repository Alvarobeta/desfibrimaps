from unittest import mock
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from unittest import mock
from thelibrary.context.library.domain.author import author_repository
from thelibrary.infrastructure.django.models import Author, Author, Category
from thelibrary.context.library.domain.author.author_repository import AuthorRepository
from thelibrary.context.library.application.get_authors.get_author_handler import GetAuthorHandler


class TestGetAuthorHandler(TestCase):

    def setUp(self) -> None:
        self.author_repository = mock.create_autospec(AuthorRepository, spec_set=True)
        self.handler = GetAuthorHandler(author_repository=self.author_repository)

    def test_get_author_returned(self):

        # author = mock.MagicMock()
        author = self.author_repository.find_one_by_id.return_value
        response = self.handler(author.id)

        self.author_repository.find_one_by_id.assert_called_with(author_id=author.id)
        self.assertEqual(response, author)

from django.test import TestCase
from unittest import mock
from thelibrary.context.library.domain.author import AuthorRepository
from thelibrary.context.library.application.create_author.create_author_handler import CreateAuthorHandler


class TestCreateAuthorHandler(TestCase):

    def setUp(self) -> None:
        self.author_repository = mock.create_autospec(AuthorRepository, spec_set=True)
        self.handler = CreateAuthorHandler(
            author_repository=self.author_repository
        )

        self.author_body = self._create_data()

    def test_create_author(self):
        created_author = self.author_repository.create.return_value

        response = self.handler(self.author_body)

        self.author_repository.create.assert_called_once_with(
            author_body=self.author_body
        )

        self.assertEqual(response.data['author'], created_author)


    @classmethod
    def _create_data(cls):
        author_body = {
            "full_name": 'Alvaro M',
            "pseudonym": 'Beta',
            "born": '1991-09-18',
        }

        return author_body

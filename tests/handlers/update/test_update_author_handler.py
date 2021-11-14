from unittest import mock
from django.test import TestCase
from thelibrary.context.library.domain.author import AuthorRepository
from thelibrary.context.library.application.update_author.update_author_handler import UpdateAuthorHandler


class TestUpdateAuthorHandler(TestCase):

    def setUp(self) -> None:
        self.author_repository = mock.create_autospec(AuthorRepository, spec_set=True)
        self.handler = UpdateAuthorHandler(
            author_repository=self.author_repository
        )

        self.author_body = self._create_data()

    def test_update_author(self):
        author = self.author_repository.find_one_by_id.return_value
        
        response = self.handler(author.id, self.author_body)

        self.author_repository.find_one_by_id.assert_called_once_with(author_id=author.id)
        self.author_repository.update.assert_called_once_with(
            author_body=self.author_body,
            author=author
        )

        self.assertEqual(response.data['author'], author)

    @classmethod
    def _create_data(cls):
        author_body = {
            "full_name": 'Peter Pettigrew',
            "pseudonym": 'Wormtail',
            "born": '1960-04-12',
        }

        return author_body

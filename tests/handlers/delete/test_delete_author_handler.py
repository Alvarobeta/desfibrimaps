from unittest import mock
from django.test import TestCase
from thelibrary.infrastructure.django.models import Author
from thelibrary.context.library.domain.author import AuthorRepository
from thelibrary.context.library.application.delete_author.delete_author_handler import DeleteAuthorHandler


class TestDeleteAuthorHandler(TestCase):

    def setUp(self) -> None:
        self.author_repository = mock.create_autospec(AuthorRepository, spec_set=True)
        self.handler = DeleteAuthorHandler(
            author_repository=self.author_repository
        )

        self.author = self._create_data()

    def test_delete_author(self):
        author = self.author_repository.find_one_by_id.return_value = self.author
        self.handler(self.author.id)

        self.author_repository.find_one_by_id.assert_called_once_with(author_id=author.id)
        self.author_repository.delete.assert_called_once_with(
            author=author
        )

    @classmethod
    def _create_data(cls):
        return Author.objects.create(
            id='11',
            full_name="Alvaro M",
            pseudonym='Beta',
            born='1991-09-18',
            died=None
        )

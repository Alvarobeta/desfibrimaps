from django.test import TestCase
from unittest import mock
from thelibrary.context.library.domain.category import CategoryRepository
from thelibrary.context.library.application.create_category.create_category_handler import CreateCategoryHandler


class TestCreateCategoryHandler(TestCase):

    def setUp(self) -> None:
        self.category_repository = mock.create_autospec(CategoryRepository, spec_set=True)
        self.handler = CreateCategoryHandler(
            category_repository=self.category_repository
        )

        self.category_body = self._create_data()

    def test_create_category(self):
        created_category = self.category_repository.create.return_value

        response = self.handler(self.category_body)

        self.category_repository.create.assert_called_once_with(
            category_body=self.category_body
        )

        self.assertEqual(response.data['category'], created_category)


    @classmethod
    def _create_data(cls):
        category_body = {
            "name": 'Terror',
            "description": 'Lots of sustos'
        }

        return category_body

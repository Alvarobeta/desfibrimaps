from unittest import mock
from django.test import TestCase
from thelibrary.context.library.domain.category import CategoryRepository
from thelibrary.context.library.application.update_category.update_category_handler import UpdateCategoryHandler


class TestUpdateCategoryHandler(TestCase):

    def setUp(self) -> None:
        self.category_repository = mock.create_autospec(CategoryRepository, spec_set=True)
        self.handler = UpdateCategoryHandler(
            category_repository=self.category_repository
        )

        self.category_body = self._create_data()

    def test_update_category(self):
        category = self.category_repository.find_one_by_id.return_value
        
        response = self.handler(category.id, self.category_body)

        self.category_repository.find_one_by_id.assert_called_once_with(category_id=category.id)
        self.category_repository.update.assert_called_once_with(
            category_body=self.category_body,
            category=category
        )

        self.assertEqual(response.data['category'], category)

    @classmethod
    def _create_data(cls):
        category_body = {
            "name": 'Romance',
            "description": 'Meh'
        }

        return category_body

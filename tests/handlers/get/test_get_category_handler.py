from unittest import mock
from django.test import TestCase
from rest_framework import status
from thelibrary.context.library.domain.category.category_repository import CategoryRepository
from thelibrary.context.library.application.get_categories.get_category_handler import GetCategoryHandler


class TestGetCategoryHandler(TestCase):

    def setUp(self) -> None:
        self.category_repository = mock.create_autospec(CategoryRepository, spec_set=True)
        self.handler = GetCategoryHandler(category_repository=self.category_repository)

    def test_get_category_returned(self):

        category = mock.Mock()
        self.category_repository.find_one_by_id.return_value = category
        response = self.handler(category.id)

        self.category_repository.find_one_by_id.assert_called_with(category_id=category.id)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.data['category'], category)

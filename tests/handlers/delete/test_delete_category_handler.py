from unittest import mock
from django.test import TestCase
from thelibrary.infrastructure.django.models import Category
from thelibrary.context.library.domain.category import CategoryRepository
from thelibrary.context.library.application.delete_category.delete_category_handler import DeleteCategoryHandler


class TestDeleteCategoryHandler(TestCase):

    def setUp(self) -> None:
        self.category_repository = mock.create_autospec(CategoryRepository, spec_set=True)
        self.handler = DeleteCategoryHandler(
            category_repository=self.category_repository
        )

        self.category = self._create_data()

    def test_delete_category(self):
        category = self.category_repository.find_one_by_id.return_value = self.category
        self.handler(self.category.id)

        self.category_repository.find_one_by_id.assert_called_once_with(category_id=category.id)
        self.category_repository.delete.assert_called_once_with(
            category=category
        )

    @classmethod
    def _create_data(cls):
        return Category.objects.create(
            id='11',
            name="Fantasy",
            description="category mock description"
        )

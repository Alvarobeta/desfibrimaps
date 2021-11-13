from unittest import mock
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from unittest import mock
from thelibrary.context.library.domain.category import category_repository
from thelibrary.infrastructure.django.models import Category, Author, Category
from thelibrary.context.library.domain.category.category_repository import CategoryRepository
from thelibrary.context.library.application.get_categories.get_categories_handler import GetCategoriesHandler


class TestGetCategoriesHandler(TestCase):

    def setUp(self) -> None:
        self.category_repository = mock.create_autospec(CategoryRepository, spec_set=True)
        self.handler = GetCategoriesHandler(category_repository=self.category_repository)

    def test_get_category_returned(self):
        categories = self.category_repository.find_categories.return_value
        response = self.handler()
        self.category_repository.find_categories.assert_called()
        self.assertEqual(response.data['categories'], categories)

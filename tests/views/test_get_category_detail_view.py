from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from thelibrary.infrastructure.django.models import Category


class GetCategoryDetailViewTest(TestCase):

    def setUp(self) -> None:
        self.endpoint = '/library/category/{category_id}'
        self.client = APIClient()
        self.category = self._create_data()
        
    def _get(self, data={}):
        return self.client.get(self.endpoint, data=data)

    def test_get_detail_ok(self):
        response = self.client.get(self.endpoint.format(category_id=self.category.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)        

    @classmethod
    def _create_data(cls):
        return Category.objects.create(
            name="Fantasy",
            description="category mock description"
        )

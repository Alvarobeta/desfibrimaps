from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from thelibrary.infrastructure.django.models import Author


class GetAuthorDetailViewTest(TestCase):

    def setUp(self) -> None:
        self.endpoint = '/library/author/{author_id}'
        self.client = APIClient()
        self.author = self._create_data()
        
    def _get(self, data={}):
        return self.client.get(self.endpoint, data=data)

    def test_get_detail_ok(self):
        response = self.client.get(self.endpoint.format(author_id=self.author.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)        

    @classmethod
    def _create_data(cls):
        return Author.objects.create(
            full_name="Alvaro M",
            pseudonym='Beta',
            born='1991-09-18',
            died=None
        )

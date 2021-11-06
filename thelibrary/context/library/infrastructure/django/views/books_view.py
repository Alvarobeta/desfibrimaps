import logging

from rest_framework import serializers

from thelibrary_core.infrastructure.django.pagination.pagination import create_paginated_response
from thelibrary_core.infrastructure.django.views.base_view import BaseView
from thelibrary_core.context.library.application.list_books.books_list_query import BooksListQuery

logger = logging.getLogger(__name__)

""" class GetBooksAuthorSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    full_name = serializers.CharField(required=True)
    pseudonym = serializers.CharField(required=False)
    born = serializers.DateField()
    died = serializers.DateField()

class GetBooksCategoriesSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False) """

class GetBooksISerializer(serializers.Serializer):
    """ isbn = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    author = GetBooksAuthorSerializer(required=True)
    catetgories = GetBooksCategoriesSerializer(required=True, many=True)
    description = serializers.CharField(required=True) """
    limit = serializers.IntegerField(required=False, min_value=1, max_value=50)
    offset = serializers.IntegerField(required=False, min_value=0) 


class BooksView(BaseView):

    def get(self, request):

        serializer_i = GetBooksISerializer(data=request.query_params)
        serializer_i.is_valid(raise_exception=True)

        """ isbn = serializer_i.validated_data['isbn']
        title = serializer_i.validated_data['title']
        author = serializer_i.validated_data['author'].get('id')
        description = serializer_i.validated_data['description']
        categories = serializer_i.validated_data['categories']"""
        limit = serializer_i.validated_data.get('limit')
        offset = serializer_i.validated_data.get('offset')

        #query = BooksListQuery(isbn=isbn, title=title, author=author, description=description, categories=categories, limit=limit, offset=offset)
        query = BooksListQuery(limit=limit, offset=offset)

        response = self.ask_query(query)

        return create_paginated_response(
            data=response.data.data,
            count=response.data.count,
            request=request,
            offset=offset,
            limit=limit
        )

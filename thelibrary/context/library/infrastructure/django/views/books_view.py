import logging

from rest_framework import serializers, response, status
from rest_framework.views import APIView

from django.shortcuts import render

from thelibrary.context.library.application.get_book import GetBookHandler
from thelibrary.context.library.domain.book import BookRepository

""" class GetBooksAuthorSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    full_name = serializers.CharField(required=True)
    pseudonym = serializers.CharField(required=False)
    born = serializers.DateField()
    died = serializers.DateField()

class GetBooksCategoriesSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False)

class GetBooksISerializer(serializers.Serializer):
     isbn = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    author = GetBooksAuthorSerializer(required=True)
    catetgories = GetBooksCategoriesSerializer(required=True, many=True)
    description = serializers.CharField(required=True) 
    limit = serializers.IntegerField(required=False, min_value=1, max_value=50)
    offset = serializers.IntegerField(required=False, min_value=0) """

# class GetBookAuthorOSerializer(serializers.Serializer):
#     id = serializers.CharField(required=False)
#     full_name = serializers.CharField(required=True)
#     pseudonym = serializers.CharField(required=False)
#     born = serializers.DateField()
#     died = serializers.DateField()

# class GetBookCategoriesOSerializer(serializers.Serializer):
#     id = serializers.CharField(required=False)
#     name = serializers.CharField(required=True)
#     description = serializers.CharField(required=False)

# class BookGetOSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     isbn = serializers.CharField()
#     title = serializers.CharField()
#     author = GetBookAuthorOSerializer()
#     description = serializers.CharField()
#     categories = GetBookCategoriesOSerializer()

class BooksView(APIView):
    def get(self, request, book_id: int):
        result = GetBookHandler.GetBook(self, book_id=book_id)
        print('BooksView ---------------------------------------------------------------------------')        


        return render(request, 'book_detail.html', {'page_obj': result})
        # return response.Response(status=status.HTTP_200_OK, data=serializer_o.data)
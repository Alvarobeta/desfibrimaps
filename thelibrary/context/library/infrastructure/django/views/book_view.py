import logging

from rest_framework import serializers, response, status
from rest_framework.views import APIView

from django.shortcuts import render

from thelibrary.context.library.application.get_book import GetBookHandler
from thelibrary.context.library.infrastructure.django.repositories.book_repository_django import BookRepositoryDjango


class BookView(APIView):
    def get(self, request, book_id: int):
        handler = GetBookHandler(book_repository=BookRepositoryDjango())
        result = handler(book_id=book_id)    

        return render(request, 'book_detail.html', {'page_obj': result})
        
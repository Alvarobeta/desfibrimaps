import logging

from rest_framework.views import APIView

from django.shortcuts import render, redirect
from thelibrary.context.library.application.create_book.create_book_handler import CreateBookHandler

from thelibrary.context.library.application.get_book import GetBookHandler
from thelibrary.context.library.infrastructure.django.repositories.book_repository_django import BookRepositoryDjango
from api.library.v1.books.views.forms import BookForm

class BooksView(APIView):
    def post(self, request):
        create_book_handler = CreateBookHandler(book_repository=BookRepositoryDjango())
        response = create_book_handler(request=request)

        if response.status_code != 201:
            error_message = "Something went wrong with the user creation, please try again"
            return render(request, 'book_create.html', {'form': BookForm(), 'error_message': error_message})

        return redirect('index')

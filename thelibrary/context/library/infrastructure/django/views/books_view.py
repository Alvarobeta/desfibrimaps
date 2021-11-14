from rest_framework.views import APIView
from rest_framework import serializers
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from thelibrary.context.library.application.create_book.create_book_handler import CreateBookHandler
from thelibrary.context.library.application.get_books.get_books_handler import GetBooksHandler
from thelibrary.context.library.infrastructure.django.repositories.author_repository_django import AuthorRepositoryDjango
from thelibrary.context.library.infrastructure.django.repositories.book_repository_django import BookRepositoryDjango
from thelibrary.context.library.infrastructure.django.repositories.category_repository_django import CategoryRepositoryDjango
from api.library.v1.books.views.forms import BookForm


class BookPostISerializer(serializers.Serializer):
    isbn = serializers.CharField()
    title = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    categories = serializers.ListField(allow_empty=False)

class BooksListView(APIView):
    def get(self, request):
        get_books_list_handler = GetBooksHandler(book_repository=BookRepositoryDjango())
        result = get_books_list_handler()    

        paginator = Paginator(result.data['books'], 10) # Show 10 Books per page.
        page_number = request.GET.get('page')
        book_list = paginator.get_page(page_number)
        
        return render(request, 'book_list.html', {'book_list': book_list})

class BooksView(APIView):
    def post(self, request):
        serializer_i = BookPostISerializer(data=request.data)

        if not serializer_i.is_valid():
            error_message = serializer_i.errors
            return render(request, 'book_create.html', {'form': BookForm(), 'error_message': error_message})

        book_body = {
            "isbn": serializer_i.validated_data['isbn'],
            "title": serializer_i.validated_data['title'],
            "author": serializer_i.validated_data['author'],
            "description": serializer_i.validated_data['description'],
            "categories": serializer_i.validated_data.get('categories')
        }

        create_book_handler = CreateBookHandler(
            author_repository=AuthorRepositoryDjango(), 
            book_repository=BookRepositoryDjango(), 
            category_repository=CategoryRepositoryDjango()
        )
        response = create_book_handler(book_body=book_body)

        if response.status_code != 201:
            error_message = "Something went wrong with the book creation, please check all required fields."
            return render(request, 'book_create.html', {'form': BookForm(), 'error_message': error_message})

        return redirect('books_view')

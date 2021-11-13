# from typing_extensions import Required
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

# class AuthorPostISerializer(serializers.Serializer):
#     full_name = serializers.CharField()
#     pseudonym = serializers.CharField()
#     born = serializers.DateField()
#     died = serializers.DateField()

# class CategoryPostISerializer(serializers.Serializer):
#     name = serializers.CharField()
#     description = serializers.CharField()

# class BookPostISerializer(serializers.Serializer):
#     isbn = serializers.CharField()
#     title = serializers.CharField()
#     # author = AuthorPostISerializer(required=True)
#     author = serializers.CharField()
#     description = serializers.CharField()
#     categories = serializers.StringListField()
    # categories = CategoryPostISerializer(required=True)

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
        book = {
            "isbn": request.data['isbn'],
            "title": request.data['title'],
            "author": request.data['author'],
            "description": request.data['description'],
            "categories": request.data.getlist('categories')
        }

        create_book_handler = CreateBookHandler(
            author_repository=AuthorRepositoryDjango(), 
            book_repository=BookRepositoryDjango(), 
            category_repository=CategoryRepositoryDjango()
        )
        response = create_book_handler(book=book)

        if response.status_code != 201:
            error_message = "Something went wrong with the book creation, please check all required fields."
            return render(request, 'book_create.html', {'form': BookForm(), 'error_message': error_message})

        return redirect('books_view')

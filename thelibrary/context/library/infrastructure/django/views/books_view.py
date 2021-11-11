from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from thelibrary.context.library.application.create_book.create_book_handler import CreateBookHandler
from thelibrary.context.library.application.get_books.get_books_handler import GetBooksHandler
from thelibrary.context.library.infrastructure.django.repositories.book_repository_django import BookRepositoryDjango
from api.library.v1.books.views.forms import BookForm


class BooksListView(APIView):
    def get(self, request):
        get_books_list_handler = GetBooksHandler(book_repository=BookRepositoryDjango())
        result = get_books_list_handler()    
        
        paginator = Paginator(result, 10) # Show 10 Books per page.
        page_number = request.GET.get('page')
        book_list = paginator.get_page(page_number)
    
        return render(request, 'book_list.html', {'book_list': book_list})

class BooksView(APIView):
    def post(self, request):
        create_book_handler = CreateBookHandler(book_repository=BookRepositoryDjango())
        response = create_book_handler(request=request)

        if response.status_code != 201:
            error_message = "Something went wrong with the book creation, please check all required fields."
            return render(request, 'book_create.html', {'form': BookForm(), 'error_message': error_message})

        return redirect('books_view')

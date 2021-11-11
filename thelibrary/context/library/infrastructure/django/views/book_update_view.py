from rest_framework.views import APIView
from django.shortcuts import render
from thelibrary.context.library.application.get_books import GetBookHandler
from thelibrary.context.library.application.update_book import UpdateBookHandler
from thelibrary.context.library.infrastructure.django.repositories.book_repository_django import BookRepositoryDjango
from api.library.v1.books.views.forms import BookForm


class BookUpdateView(APIView):
    def get(self, request, book_id: int):
        get_book_handler = GetBookHandler(book_repository=BookRepositoryDjango())
        result = get_book_handler(book_id=book_id)    

        return render(request, 'book_update.html', {'form': BookForm(instance=result)})
        
    def put(self, request, book_id: int):        
        update_book_handler = UpdateBookHandler(book_repository=BookRepositoryDjango())
        response = update_book_handler(request=request, book_id=book_id)  
        
        if response.status_code != 201:
            error_message = "Something went wrong with the book update, please check all required fields."
            return render(request, 'book_update.html', {'form': BookForm(), 'error_message': error_message})

        return render(request, 'book_detail.html', {'page_obj': response.data['book']})

from rest_framework.views import APIView
from django.shortcuts import render
from thelibrary.context.library.application.get_books import GetBookHandler
from thelibrary.context.library.application.delete_book import DeleteBookHandler
from thelibrary.context.library.infrastructure.django.repositories.book_repository_django import BookRepositoryDjango


class BookView(APIView):
    def get(self, request, book_id: int):
        get_book_handler = GetBookHandler(book_repository=BookRepositoryDjango())
        result = get_book_handler(book_id=book_id)    

        return render(request, 'book_detail.html', {'page_obj': result.data['book']})
        
    def delete(self, request, book_id: int):
        delete_book_handler = DeleteBookHandler(book_repository=BookRepositoryDjango())
        
        return delete_book_handler(book_id=book_id)

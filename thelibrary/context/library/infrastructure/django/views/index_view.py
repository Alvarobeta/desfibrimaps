from rest_framework.views import APIView
from django.shortcuts import render
from thelibrary.context.library.application.get_index.get_index_handler import GetIndexHandler
from thelibrary.context.library.infrastructure.django.repositories.author_repository_django import AuthorRepositoryDjango
from thelibrary.context.library.infrastructure.django.repositories.book_repository_django import BookRepositoryDjango
from thelibrary.context.library.infrastructure.django.repositories.category_repository_django import CategoryRepositoryDjango


class IndexView(APIView):
    def get(self, request):
        get_index_handler = GetIndexHandler(
            author_repository=AuthorRepositoryDjango(), 
            book_repository=BookRepositoryDjango(), 
            category_repository=CategoryRepositoryDjango()
        )
        result = get_index_handler()    

        return render(request, 'index.html', {'counts_data': result.data})

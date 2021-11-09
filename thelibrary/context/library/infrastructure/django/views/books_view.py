import logging

from rest_framework.views import APIView

from django.shortcuts import render, redirect

from thelibrary.context.library.application.get_book import GetBookHandler
from thelibrary.context.library.infrastructure.django.repositories.book_repository_django import BookRepositoryDjango
from api.library.v1.books.views.forms import BookForm

class BooksView(APIView):
    def get(self, request):
        return render(request, 'create_book.html', {'form': BookForm()})

    def post(self, request):
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = BookForm()

        return render(request, 'create_book.html', {'form': form})

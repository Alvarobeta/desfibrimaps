from django.views import generic
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
#from .infrastructure.django.models import DjangoDea
""" from .forms import DeaForm
from .forms import NearestDeaForm """
from django.db.models import Q, F
import math

from thelibrary.infrastructure.django.models.book import Book

def index(request):
    books = Book.objects.all()

    paginator = Paginator(books, 10) # Show 10 Books per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})

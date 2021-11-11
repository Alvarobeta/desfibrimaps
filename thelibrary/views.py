from django.shortcuts import render
from django.core.paginator import Paginator
from thelibrary.context.library.infrastructure.django.views.index_view import IndexView as IndexViewCore


def index(request):
    return IndexViewCore().get(
        request=request
    )

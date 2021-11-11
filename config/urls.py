"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from thelibrary import views
from api.library.v1.books.views.book_view import BookView
from api.library.v1.books.views.book_update_view import BookUpdateView
from api.library.v1.books.views.books_view import BooksListView, BooksView
from api.library.v1.authors.views.authors_view import AuthorsListView, AuthorsView
from api.library.v1.authors.views.author_view import AuthorView
from api.library.v1.authors.views.author_update_view import AuthorUpdateView
from api.library.v1.categories.views.categories_view import CategoriesListView, CategoriesView
from api.library.v1.categories.views.category_view import CategoryView
from api.library.v1.categories.views.category_update_view import CategoryUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', views.index, name='index'),
    
    url(
        r'^library/books/?$',
        BooksListView.as_view(),
        name='books_view'
    ),
    url(r'^library/book/(?P<book_id>[0-9]+)/?$',
        BookView.as_view(),
        name='book_view'
    ),
    url(r'^library/book/(?P<book_id>[0-9]+)/update/?$',
        BookUpdateView.as_view(),
        name='book_update'
    ),
    url(r'^library/book/(?P<book_id>[0-9]+)/delete/?$',
        BookView.as_view(),
        name='book_delete'
    ),
    url(
        r'^library/book/create/?$',
        BooksView.as_view(),
        name='book_create'
    ),
    url(
        r'^library/author/(?P<author_id>[0-9]+)/?$',
        AuthorView.as_view(),
        name='author_view'
    ),
    url(
        r'^library/author/(?P<author_id>[0-9]+)/update/?$',
        AuthorUpdateView.as_view(),
        name='author_update'
    ),
    url(
        r'^library/author/(?P<author_id>[0-9]+)/delete/?$',
        AuthorView.as_view(),
        name='author_delete'
    ),
    url(
        r'^library/author/create/?$',
        AuthorsView.as_view(),
        name='author_create'
    ),
    url(
        r'^library/authors/?$',
        AuthorsListView.as_view(),
        name='authors_view'
    ),
        url(
        r'^library/categories/?$',
        CategoriesListView.as_view(),
        name='categories_view'
    ),
    url(
        r'^library/category/create/?$',
        CategoriesView.as_view(),
        name='category_create'
    ),
    url(
        r'^library/category/(?P<category_id>[0-9]+)/?$',
        CategoryView.as_view(),
        name='category_view'
    ),
    url(
        r'^library/category/(?P<category_id>[0-9]+)/update/?$',
        CategoryUpdateView.as_view(),
        name='category_update'
    ),
    url(
        r'^library/category/(?P<category_id>[0-9]+)/delete/?$',
        CategoryView.as_view(),
        name='category_delete'
    )
]

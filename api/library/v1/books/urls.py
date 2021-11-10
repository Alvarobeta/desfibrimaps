"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path

from api.library.v1.books.views.book_view import BookView
from api.library.v1.books.views.books_view import BooksView


# urlpatterns = [
#     url(
#         r'^books/<str:book_id>/',
#         BookView.as_view(),
#         name='books_list_view'
#     ),
#     url(
#         r'^books/?$',
#         BooksView.as_view(),
#         name='create_book'
#     ),
# ]

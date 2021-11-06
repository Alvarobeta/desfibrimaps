""" from typing import List
from enum import Enum """
from thelibrary_core.domain.bus.query.query import Query
""" from thelibrary_core.context.shared.infrastructure.django.models.author import Author
from thelibrary_core.context.shared.infrastructure.django.models.category import Category
 """

class BooksListQuery(Query):

    def __init__(
        self,
        offset: int,
        limit: int,
        #isbn: str,
        #title: str,
        #author: Author,
        #description: str,
        #categories: List[Category]
    ):
        self.limit = limit
        self.offset = offset
        #isbn = isbn
        #title = title
        #author = author
        #description = description
        #categories = categories

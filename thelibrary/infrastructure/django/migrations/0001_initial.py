import json
import os
import uuid

from typing import Optional

from django.db import migrations, models

from thelibrary.infrastructure.django.models.author import Author
from thelibrary.infrastructure.django.models.book import Book
from thelibrary.infrastructure.django.models.category import Category


def load_data(apps, schema_editor):
    json_data: Optional[dict] = None

    file_path = f'{os.path.abspath(os.path.dirname(__name__))}/data/the_library.json'
    with open(file_path, 'r') as the_library_json:
        json_data = json.load(the_library_json)

    for author_data in json_data.get('authors'):
        Author.objects.create(
            full_name=author_data.get('full_name'),
            pseudonym=author_data.get('pseudonym'),
            born=author_data.get('born'),
            died=author_data.get('died')
        )

    for category_data in json_data.get('categories'):
        Category.objects.create(
            name=category_data.get('name'),
            description=category_data.get('category')
        )

    for book_data in json_data.get('books'):

        author = Author.objects.get(full_name=book_data.get('author'))
        categories_names = book_data.get('categories')
        categories = Category.objects.filter(name__in=categories_names)

        book = Book.objects.create(
            isbn=book_data.get('isbn'),
            title= book_data.get('title'),
            author=author,
            description=book_data.get('description')
        )
        book.categories.set(categories)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('pseudonym', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('born', models.DateField(blank=True, null=True)),
                ('died', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(
                    blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.ForeignKey('Author',
                 db_column='author_id', on_delete=models.SET_NULL, null=True)),
                ('description', models.CharField(max_length=500)),
                ('categories', models.ManyToManyField( to='thelibrary.Category')),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.RunPython(load_data),
    ]

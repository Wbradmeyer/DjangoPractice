from django.urls import path
from . import views

app_name = 'books_authors'

urlpatterns = [
    path('', views.index),
    path('books/create', views.create_book, name='new_book'),
    path('books/<int:book_id>', views.show_book, name='display_book'),
    path('books/add_author', views.add_author, name='add_author'),
    path('authors', views.author_index),
    path('authors/create', views.create_author, name='new_author'),
    path('authors/<int:author_id>', views.show_author, name='display_author'),
    path('author/add_book', views.add_book, name='add_book'),
]
from django.shortcuts import render, redirect
from .models import Book
from .models import Author

# Create your views here.

# Create methods

def create_book(request):
    Book.objects.create(title = request.POST['title'],
                        desc = request.POST['desc'])
    return redirect('/')

def create_author(request):
    Author.objects.create(first_name = request.POST['first_name'],
                        last_name = request.POST['last_name'],
                        notes = request.POST['notes'])
    return redirect('/authors')


# Read methods

def index(request):
    content = {
        'all_books': Book.objects.all()
    }
    return render(request, 'index.html', content)

def author_index(request):
    content = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'new_author.html', content)

def show_book(request, book_id):
    content = {
        'book': Book.objects.get(id=book_id),
        'all_authors': Author.objects.all()
    }
    return render(request, 'one_book.html', content)

def show_author(request, author_id):
    content = {
        'author': Author.objects.get(id=author_id),
        'all_books': Book.objects.all()
    }
    return render(request, 'one_author.html', content)

def add_author(request):
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_book.authors.add(this_author)
    return redirect(f'/books/{this_book.id}')

def add_book(request):
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_author.books.add(this_book)
    return redirect(f'/authors/{this_author.id}')
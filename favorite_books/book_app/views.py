from django.shortcuts import render, redirect
from django.contrib import messages
from user_app.models import User
from book_app.models import Book

# Create your views here.
def dashboard(request):
    content = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_books': Book.objects.all()
    }
    return render(request, 'dashboard.html', content)

def create_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        this_user = User.objects.get(id=request.session['user_id'])
        this_book = Book.objects.create(title=request.POST['title'],
                                desc=request.POST['desc'],
                                uploaded_by=this_user)
        this_book.users_who_like.add(this_user)
        this_book.save()
        return redirect('/books')
    
def display_book(request, book_id):
    content = {
        'user': User.objects.get(id=request.session['user_id']),
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'display_book.html', content)

def update_book(request, book_id):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/books/{book_id}')
    else:
        book = Book.objects.get(id=book_id)
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.save()
    return redirect('/books')

def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect('/books')

def like_book(request, book_id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    book.users_who_like.add(user)
    book.save()
    return redirect('/books')

def unlike_book(request, book_id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    book.users_who_like.remove(user)
    book.save()
    return redirect('/books')
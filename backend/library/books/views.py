from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book

# Display the all books


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def details(request, book_id):
    return HttpResponse("test" + str(book_id))

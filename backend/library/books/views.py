from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book


# Display the all books
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


# Display a specific book
def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/details.html', {'book': book})


# Create a book
def create(request):
    name = request.POST['name']
    author = request.POST['author']
    publisher = request.POST['publisher']
    date_pub = request.POST['date_pub']
    book = Book(name=name, author=author,
                publisher=publisher, date_pub=date_pub)
    book.save()
    return HttpResponse(name + " " + author + " " + publisher + " " + date_pub)

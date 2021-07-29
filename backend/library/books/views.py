from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Book
import json


# Display the all books
def index(request):
    books = Book.objects.all().values()
    # return render(request, 'books/index.html', {'books': books})
    return JsonResponse({'books': list(books)})



# Display a specific book
def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    serialized_book = serializers.serialize('json', [book, ])
    before_book = json.loads(serialized_book)[0]["fields"]
    return JsonResponse({'book': before_book})

# Create a book
def create(request):
    name = request.POST['name']
    author = request.POST['author']
    publisher = request.POST['publisher']
    ISBN = request.POST['ISBN']
    date_pub = request.POST['date_pub']
    book = Book(name=name, author=author,
                publisher=publisher, date_pub=date_pub, ISBN=ISBN)
    book.save()
    books = Book.objects.all().values()
    # return HttpResponseRedirect('/books/')
    return JsonResponse({'books': list(books)})

# Delete a book
def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    books = Book.objects.all().values()
    # return HttpResponseRedirect('/books/')
    return JsonResponse({'books': list(books)})


# Update a book
def update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.name = request.POST['name']
    book.author = request.POST['author']
    book.publisher = request.POST['publisher']
    book.ISBN = request.POST['ISBN']
    book.date_pub = request.POST['date_pub']
    book.save()
    books = Book.objects.all().values()
    # return HttpResponseRedirect('/books/')
    return JsonResponse({'books': list(books)})


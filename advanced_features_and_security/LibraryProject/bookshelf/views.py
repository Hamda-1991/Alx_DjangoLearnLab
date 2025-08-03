from django.shortcuts import render,  get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
# Create your views here.
# bookshelf/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Bookshelf App!")


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # form handling code here
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # form handling code here
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # delete logic here
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
from django.shortcuts import render,  get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm  # You’ll create this form below
from django.db.models import Q
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


def form_example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # process form data
            pass
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

def search_books(request):
    query = request.GET.get('q')
    results = []
    if query:
        # Safe query using Django ORM
        results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'bookshelf/book_list.html', {'results': results})
# This view uses CSRF protection via Django's built-in middleware.
# We use Django forms to validate inputs and avoid XSS/SQL injection.

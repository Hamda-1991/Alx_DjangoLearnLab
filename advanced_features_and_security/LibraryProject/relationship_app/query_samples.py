import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)       # ✅ REQUIRED
books = Book.objects.filter(author=author)          # ✅ REQUIRED
print("Books by", author_name, ":", [book.title for book in books])

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)    # ✅ REQUIRED
books = library.books.all()
print("Books in", library_name, ":", [book.title for book in books])

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian of", library.name, ":", librarian.name)

"""
BookListView with filtering, searching, and ordering:
- Filtering: title, author, publication_year
- Searching: title, author
- Ordering: title, publication_year (default: title)
"""
from rest_framework import generics, permissions, filters
  # ✅ Required import
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer

# List all books (GET) - accessible by anyone
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]


    # Fields for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields for searching
    search_fields = ['title', 'author']

    # Fields for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

# Retrieve a single book by ID (GET) - accessible by anyone
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book (POST) - authenticated users only
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Update an existing book (PUT/PATCH) - authenticated users only
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete a book (DELETE) - authenticated users only
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

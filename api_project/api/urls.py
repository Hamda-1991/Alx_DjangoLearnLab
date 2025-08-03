from django.urls import path, include
from .views import BookList, BookViewSet  # Make sure BookViewSet is imported
from rest_framework.routers import DefaultRouter

# Create the router and register the ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),  # Include all CRUD routes
]

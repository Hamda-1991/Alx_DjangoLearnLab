# Token Authentication endpoint using DRF's built-in view
# POST to /api-token-auth/ to receive a token

from django.urls import path, include
from .views import BookList, BookViewSet  # Make sure BookViewSet is imported
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Create the router and register the ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),  # Include all CRUD routes
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

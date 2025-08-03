"""
This API uses Token Authentication (DRF).
Only authenticated users can access the BookViewSet endpoints.

To get a token:
POST to /api-token-auth/ with valid username and password.

Include the token in requests like:
Authorization: Token your_token_here
"""
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
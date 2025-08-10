from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone


# BookSerializer:
# Serializes all fields of the Book model with validation.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to ensure year is not in the future
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer:
# Serializes Author model with nested BookSerializer for related books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested books, read-only

    class Meta:
        model = Author
        fields = ['name', 'books']

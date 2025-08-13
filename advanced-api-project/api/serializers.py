from rest_framework import serializers
<<<<<<< HEAD
from .models import Author, Book
from datetime import date
=======
from django.utils import timezone
from .models import Author, Book
>>>>>>> 75cbce5 (add)

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields.
    Includes validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        # export id, title, publication_year and author (author is FK id)
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    books = BookSerializer(many=True, read_only=True)  # nested serializer
=======
    """
    Serializes Author model and nests the related books using BookSerializer.
    The 'books' field comes from Book.author related_name='books'.
    """
    books = BookSerializer(many=True, read_only=True)
>>>>>>> 75cbce5 (add)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

from django.db import models

# Author model:
# Stores an author's name.
class Author(models.Model):
    name = models.CharField(max_length=100, help_text="The author's full name.")

    def __str__(self):
        return self.name


# Book model:
# Represents a book with a title, publication year, and an associated author.
class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the book.")
    publication_year = models.IntegerField(help_text="Year the book was published.")
    author = models.ForeignKey(
        Author,
        related_name='books',  # Enables reverse lookup: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


# Create your models here.

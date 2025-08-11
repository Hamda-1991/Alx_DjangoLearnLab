from django.db import models

# Create your models here.


class Author(models.Model):
    """
    Author model: stores an author's name.
    One Author can have many Books (one-to-many).
    """
    name = models.CharField(max_length=100, help_text="Author's full name")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model: title, publication_year, and foreign key to Author.
    The related_name 'books' allows reverse lookup: author.books.all()
    """
    title = models.CharField(max_length=200, help_text="Title of the book")
    publication_year = models.IntegerField(help_text="Year the book was published")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

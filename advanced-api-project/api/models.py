from django.db import models
from django.utils import timezone
# Create your models here.

<<<<<<< HEAD
class Author(models.Model):
    name = models.CharField(max_length=100)
=======
# Create your models here.


class Author(models.Model):
    """
    Author model: stores an author's name.
    One Author can have many Books (one-to-many).
    """
    name = models.CharField(max_length=100, help_text="Author's full name")
>>>>>>> 75cbce5 (add)

    def __str__(self):
        return self.name


class Book(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
=======
    """
    Book model: title, publication_year, and foreign key to Author.
    The related_name 'books' allows reverse lookup: author.books.all()
    """
    title = models.CharField(max_length=200, help_text="Title of the book")
    publication_year = models.IntegerField(help_text="Year the book was published")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
>>>>>>> 75cbce5 (add)

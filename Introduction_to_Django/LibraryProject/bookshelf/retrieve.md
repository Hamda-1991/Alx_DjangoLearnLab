from bookshelf.models import Book
books = Book.objects.all()
for b in books:
print(b)

# 1984 by George Orwell (1949)

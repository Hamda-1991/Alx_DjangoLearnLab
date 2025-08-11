from django.contrib import admin
from .models import Author, Book
# Register your models here.


# Register models so you can manage them in Django admin
admin.site.register(Author)
admin.site.register(Book)

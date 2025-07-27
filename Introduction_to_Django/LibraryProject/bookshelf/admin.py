from django.contrib import admin

# Register your models here.

from .models import Book  # Import the Book model

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show in list view
    list_filter = ('publication_year',)  # Add filter by year
    search_fields = ('title', 'author')  # Enable search

# Register the model and the admin config
admin.site.register(Book, BookAdmin)

from django.contrib import admin

from books.models import Book, BookCategory, BookAuthor

admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(BookAuthor)

# Register your models here.

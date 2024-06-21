from rest_framework import serializers

from books.models import Book, BookAuthor, BookCategory 


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = [
            'title',
            'release_year',
            'quantity',
            'author',
            'category'
        ]

class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = [
            'name',
        ]

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = [
            'name',
        ]

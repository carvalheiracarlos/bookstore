from rest_framework import serializers

from books.models import Book, BookAuthor, BookCategory 


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = [
            'id',
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
            'id',
            'name',
        ]

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = [
            'id',
            'name',
        ]

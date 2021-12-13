from rest_framework import serializers
from ..models.author import Author
from .book import BookSerializer

class AuthorSerializer(serializers.ModelSerializer):
  books = BookSerializer(many=True, read_only=True)
  class Meta:
    model = Author
    fields = ('id', 'first_name', 'last_name', 'books')
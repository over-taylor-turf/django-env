from rest_framework import serializers
from ..models.book import Book
from ..models.author import Author

class BookSerializer(serializers.ModelSerializer):
     # Define meta class
    class Meta:
         # Specify the model from which to define the fields
        model = Book
        # Define fields to be returned
        fields = '__all__'
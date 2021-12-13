from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.book import BookSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.book import Book
from django.views import View
import json

class BooksView(APIView):
    # POST request to create a new book
    # POST / books
    def post(self, request):
        book = BookSerializer(data=request.data)
        if book.is_valid():
             book.save()
             return Response(book.data, status=status.HTTP_201_CREATED)
        else:
            return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET request for all books
    # GET /books "INDEX"
    def get(self, request):
        books = Book.objects.all()
        data = BookSerializer(books, many=True).data
        return Response(data)



class BookView(APIView):
    # GET request for a specific book by id
    # GET /books/:id "SHOW"
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        data = BookSerializer(book).data
        return Response(data)
    
    # DELETE
    def delete(self, request, id):
        book = get_object_or_404(Book, id=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # UPDATE
    def patch(self, request, id): 
        book = get_object_or_404(Book, id=id)
        updated_book = BookSerializer(book, data=request.data, partial=True)
        if updated_book.is_valid():
            updated_book.save()
            return Response(updated_book.data)
    
    # UPDATE
    def put(self, request, id): 
        book = get_object_or_404(Book, id=id)
        updated_book = BookSerializer(book, data=request.data)
        if updated_book.is_valid():
            updated_book.save()
            return Response(updated_book.data)


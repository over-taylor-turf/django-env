from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.author import AuthorSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.author import Author
from django.views import View
import json

# /books
class AuthorsView(APIView):
    # POST / authors
    def post(self, request):
        author = AuthorSerializer(data=request.data)
        if author.is_valid():
             author.save()
             return Response(author.data, status=status.HTTP_201_CREATED)
        else:
            return Response(author.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET /authors
    def get(self, request):
        authors = Author.objects.all()
        data = AuthorSerializer(authors, many=True).data
        return Response(data)

# /authors/:id
class AuthorView(APIView):
    
    def patch(self, request, id):
        author = get_object_or_404(Author, id=id)
        updated_author = AuthorSerializer(author, data=request.data, partial=True)
        if updated_author.is_valid():
            updated_author.save()
            return Response(updated_author.data)
    
    def put(self, request, id):
        author = get_object_or_404(Author, id=id)
        updated_author = AuthorSerializer(author, data=request.data)
        if updated_author.is_valid():
            updated_author.save()
            return Response(updated_author.data)
    
    def delete(self, request, id):
        author = get_object_or_404(Author, id=id)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # GET /authors/:id
    def get(self, request, id):
        author = get_object_or_404(Author, id=id)
        data = AuthorSerializer(author).data
        return Response(data)
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.gift import GiftSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.gift import Gift
from django.views import View
import json

class GiftsView(APIView):
    # POST request to create a new book
    # POST / books
    def post(self, request):
        gift = GiftSerializer(data=request.data)
        if gift.is_valid():
             gift.save()
             return Response(gift.data, status=status.HTTP_201_CREATED)
        else:
            return Response(gift.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # GET request for all books
    # GET /books "INDEX"
    def get(self, request):
        gifts = Gift.objects.all()
        data = GiftSerializer(gifts, many=True).data
        return Response(data)

class GiftView(APIView):
    # GET request for a specific book by id
    # GET /books/:id "SHOW"
    def get(self, request, id):
        gift = get_object_or_404(Gift, id=id)
        data = GiftSerializer(gift).data
        return Response(data)

    # DELETE
    def delete(self, request, id):
        gift = get_object_or_404(Gift, id=id)
        gift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # UPDATE
    def patch(self, request, id): 
        gift = get_object_or_404(Gift, id=id)
        updated_gift = GiftSerializer(gift, data=request.data, partial=True)
        if updated_gift.is_valid():
            updated_gift.save()
            return Response(updated_gift.data)
    
    # UPDATE
    def put(self, request, id): 
        gift = get_object_or_404(Gift, id=id)
        updated_gift = GiftSerializer(gift, data=request.data)
        if updated_gift.is_valid():
            updated_gift.save()
            return Response(updated_gift.data)
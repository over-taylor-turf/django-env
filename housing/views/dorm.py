from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.dorm import DormSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.dorm import Dorm
from django.views import View
import json


class DormsView(APIView):
    # POST request to create a new book
    # POST / books
    def post(self, request):
        dorm = DormSerializer(data=request.data)
        if dorm.is_valid():
             dorm.save()
             return Response(dorm.data, status=status.HTTP_201_CREATED)
        else:
            return Response(dorm.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET request for all books
    # GET /books "INDEX"
    def get(self, request):
        dorms = Dorm.objects.all()
        data = DormSerializer(dorms, many=True).data
        return Response(data)

class DormView(APIView):
    # GET request for a specific book by id
    # GET /books/:id "SHOW"
    def get(self, request, id):
        dorm = get_object_or_404(Dorm, id=id)
        data = DormSerializer(dorm).data
        return Response(data)

    # DELETE
    def delete(self, request, id):
        dorm = get_object_or_404(Dorm, id=id)
        dorm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # UPDATE
    def patch(self, request, id): 
        dorm = get_object_or_404(Dorm, id=id)
        updated_dorm = DormSerializer(dorm, data=request.data, partial=True)
        if updated_dorm.is_valid():
            updated_dorm.save()
            return Response(updated_dorm.data)
        
    # UPDATE
    def put(self, request, id): 
        dorm = get_object_or_404(Dorm, id=id)
        updated_dorm = DormSerializer(dorm, data=request.data)
        if updated_dorm.is_valid():
            updated_dorm.save()
            return Response(updated_dorm.data)
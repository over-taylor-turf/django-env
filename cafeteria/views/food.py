from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.food import FoodSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.food import Food
from django.views import View
import json


class FoodsView(APIView):
    # POST request to create a new book
    # POST / books
    def post(self, request):
        food = FoodSerializer(data=request.data)
        if food.is_valid():
             food.save()
             return Response(food.data, status=status.HTTP_201_CREATED)
        else:
            return Response(food.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET request for all books
    # GET /books "INDEX"
    def get(self, request):
        foods = Food.objects.all()
        data = FoodSerializer(foods, many=True).data
        return Response(data)


class FoodView(APIView):
    # GET request for a specific book by id
    # GET /books/:id "SHOW"
    def get(self, request, id):
        food = get_object_or_404(Food, id=id)
        data = FoodSerializer(food).data
        return Response(data)

    # DELETE
    def delete(self, request, id):
        food = get_object_or_404(Food, id=id)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # UPDATE... PATCH
    def patch(self, request, id): 
        food = get_object_or_404(Food, id=id)
        updated_food = FoodSerializer(food, data=request.data, partial=True)
        if updated_food.is_valid():
            updated_food.save()
            return Response(updated_food.data)
        # else:
        #     return Response(updated_food.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # UPDATE... PUT
    def put(self, request, id): 
        food = get_object_or_404(Food, id=id)
        updated_food = FoodSerializer(food, data=request.data)
        if updated_food.is_valid():
            updated_food.save()
            return Response(updated_food.data)
        # else:
        #     return Response(updated_food.errors, status=status.HTTP_400_BAD_REQUEST)
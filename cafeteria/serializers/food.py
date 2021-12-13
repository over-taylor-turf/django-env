from rest_framework import serializers
from ..models.food import Food

class FoodSerializer(serializers.ModelSerializer):
     # Define meta class
    class Meta:
         # Specify the model from which to define the fields
        model = Food
        # Define fields to be returned
        fields = '__all__'
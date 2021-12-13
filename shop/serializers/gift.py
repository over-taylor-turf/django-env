from rest_framework import serializers
from ..models.gift import Gift

class GiftSerializer(serializers.ModelSerializer):
     # Define meta class
    class Meta:
         # Specify the model from which to define the fields
        model = Gift
        # Define fields to be returned
        fields = '__all__'
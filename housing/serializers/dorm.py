from rest_framework import serializers
from ..models.dorm import Dorm

class DormSerializer(serializers.ModelSerializer):

     # Define meta class
    class Meta:

         # Specify the model from which to define the fields
        model = Dorm

        # Define fields to be returned
        fields = '__all__'
from rest_framework import serializers
from ..models.doctor import Doctor

class DoctorSerializer(serializers.ModelSerializer):
     # Define meta class
    class Meta:
         # Specify the model from which to define the fields
        model = Doctor
        # Define fields to be returned
        fields = '__all__'
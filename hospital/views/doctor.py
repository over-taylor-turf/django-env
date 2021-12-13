from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.doctor import DoctorSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.doctor import Doctor
from django.views import View
import json

class DoctorsView(APIView):
    # POST request to create a new book
    # POST / books
    def post(self, request):
        doctor = DoctorSerializer(data=request.data)
        if doctor.is_valid():
             doctor.save()
             return Response(doctor.data, status=status.HTTP_201_CREATED)
        else:
            return Response(doctor.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET request for all books
    # GET /books "INDEX"
    def get(self, request):
        doctors = Doctor.objects.all()
        data = DoctorSerializer(doctors, many=True).data
        return Response(data)

# def index(request):
#     doctors = Doctor.objects.all()
#     data = {
#         "doctors": list(doctors.values())
#     }
#     return JsonResponse(data)

# def show(request, id):
#     doctor = Doctor.objects.get(id=id).as_dict()
#     return JsonResponse(doctor)

class DoctorView(APIView):
    # GET request for a specific book by id
    # GET /books/:id "SHOW"
    def get(self, request, id):
        doctor = get_object_or_404(Doctor, id=id)
        data = DoctorSerializer(doctor).data
        return Response(data)
    
    # DELETE
    def delete(self, request, id):
        doctor = get_object_or_404(Doctor, id=id)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # UPDATE
    def patch(self, request, id): 
        doctor = get_object_or_404(Doctor, id=id)
        updated_doctor = DoctorSerializer(doctor, data=request.data, partial=True)
        if updated_doctor.is_valid():
            updated_doctor.save()
            return Response(updated_doctor.data)
    
    # UPDATE
    def put(self, request, id): 
        doctor = get_object_or_404(Doctor, id=id)
        updated_doctor = DoctorSerializer(doctor, data=request.data)
        if updated_doctor.is_valid():
            updated_doctor.save()
            return Response(updated_doctor.data)
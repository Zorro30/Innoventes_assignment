from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializers
from .models import Employee_details
# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee_details.objects.all()
    serializer_class = EmployeeSerializers

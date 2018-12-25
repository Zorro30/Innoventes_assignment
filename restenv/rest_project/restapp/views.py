from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializers
from .serializers import AddressSerializers
from .models import Employee_details
# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee_details.objects.all()
    serializer_class = EmployeeSerializers

class EmployeeAddress(viewsets.ModelViewSet):

    queryset = Employee_details.objects.all().values('First_name','Present_Address','Permanent_Address','Office_Address')
    serializer_class = AddressSerializers
from .models import Employee_details
from rest_framework import  serializers

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee_details
        fields = ('id','First_name','Last_name','Date_of_Birth','Address')

from django.db import models

class Employee_details(models.Model):
    First_name = models.CharField(max_length = 200)
    Last_name = models.CharField(max_length = 200)
    Date_of_Birth = models.CharField(max_length = 200)
    Present_Address = models.CharField(max_length = 200, blank = True,)
    Permanent_Address = models.CharField(max_length = 200, blank = True,)
    Office_Address = models.CharField(max_length = 200, blank = True,)

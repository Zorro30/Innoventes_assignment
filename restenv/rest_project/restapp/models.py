from django.db import models

class Employee_details(models.Model):
    First_name = models.CharField(max_length = 200)
    Last_name = models.CharField(max_length = 200)
    Date_of_Birth = models.CharField(max_length = 200)
    Address_Present = models.CharField(max_length = 200, blank = True,)
    Address_Permanent = models.CharField(max_length = 200, blank = True,)
    Address_Office = models.CharField(max_length = 200, blank = True,)
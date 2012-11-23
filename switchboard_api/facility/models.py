from django.db import models

# Create your models here.
class facility(models.Model):
    name_of_facility=models.CharField(max_length=100)
    type_of_facility = models.CharField(max_length=50)
    town = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    postal_address = models.CharField(max_length=50,null=True)
    email_address = models.EmailField(null=True)
    telephone_number = models.CharField(max_length=20, null=True)

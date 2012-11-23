from django.db import models

# Create your models here.
class contact(models.Model):
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=10, choices=gender_option)
    date_of_birth = models.DateField(null=True)
    nationality = models.CharField(max_length=30,null=True)
    postal_address = models.CharField(max_length=100,null=True)
    vodacom_phone = models.IntegerField(null=True)
    other_phone = models.IntegerField(null=True)
    email_address = models.EmailField(null=True)

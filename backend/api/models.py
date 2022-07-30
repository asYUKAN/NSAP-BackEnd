from django.db import models

# Create your models here.
class Applicant(models.Model):
    Name=models.CharField(max_length=50)
    FName=models.CharField(max_length=50)
    Gender=models.CharField(max_length=20)
    DOB=models.DateField()
    Age=models.IntegerField()

    Category=models.CharField( max_length=10)

    
    Ward=models.CharField(max_length=50)
    SubDistrict=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    State=models.CharField(max_length=25)
    
    Pincode=models.IntegerField()
    

   
    
    
    
    Mobile=models.BigIntegerField()
    AadharNo=models.BigIntegerField()
    Disablity=models.CharField( max_length=3)
    DisabilityType=models.TextField()
    BPL_Family_ID=models.CharField(max_length=50)
    BankDetails=models.TextField()
    IGNOAPS=models.CharField(max_length=3,default="")
    IGNWPS=models.CharField(max_length=3,default="")
    IGNDPS=models.CharField(max_length=3,default="")
    NFBS=models.CharField(max_length=3,default="")


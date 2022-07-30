from django.contrib import admin
from .models import *
# Register your models here.
class ApplicantAdmin(admin.ModelAdmin):
    list_display=['id','Name','FName','Gender','DOB','Age','Category','Ward','SubDistrict','District','State','Pincode','Mobile','AadharNo','Disablity','DisabilityType','BPL_Family_ID','BankDetails','IGNOAPS','IGNWPS','IGNDPS','NFBS']



admin.site.register(Applicant,ApplicantAdmin)


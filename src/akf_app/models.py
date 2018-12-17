from django.db import models
from datetime import datetime
from django.utils import timezone

# Model classes for DB tables
class Geo_Information(models.Model):
    id = models.AutoField(primary_key=True)
    district = models.CharField(max_length=255, default=None)
    block = models.CharField(max_length=255, default=None)
    cluster = models.CharField(max_length=255, default=None)
    gram_panchayat = models.CharField(max_length=255, default=None)
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'geo_information'


class Student_Report(models.Model):
    id = models.AutoField(primary_key=True)
    district_id = models.ForeignKey(Geo_Information, db_column='district_id', on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255, default=None)
    addition = models.IntegerField(default=0)
    subtraction = models.IntegerField(default=0)
    product = models.IntegerField(default=0)
    division = models.IntegerField(default=0)
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now) 
    
    class Meta:
        db_table = 'student_report'       
    

from django.db import models
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify


class Candidate(models.Model):
    roll = models.CharField(max_length=9 , unique = True)#CharField?
    cat = models.CharField(default="GE")
    pd = models.BooleanField(default=False)
    
    # program=models.Field(max_length=4,min_length=4)
#     institue=models.CharField(max_length=1)
    
    def __str__(self):
        return self.roll
        
   

    
class Preference(models.Model):
    candidate = models.ForeignKey(Candidate)
    institute = models.CharField(max_length=1)
    program = models.CharField(max_length=4)
    class Meta:
         unique_together = (("candidate","program"))
################################################################

class Program(models.Model):
    institute=models.CharField(max_length=128)
    department=models.CharField(max_length=128)
    code1=models.CharField(max_length=5)
    #cat=models.IntegerField()
    openrank1=models.IntegerField()
    closerank1=models.IntegerField()
    openrank2=models.IntegerField()
    closerank2=models.IntegerField()
    openrank3=models.IntegerField()
    closerank3=models.IntegerField()
    openrank4=models.IntegerField()
    closerank4=models.IntegerField()
    openrank5=models.IntegerField()
    closerank5=models.IntegerField()
    openrank6=models.IntegerField()
    closerank6=models.IntegerField()
    openrank7=models.IntegerField()
    closerank7=models.IntegerField()
    openrank8=models.IntegerField()
    closerank8=models.IntegerField()
    
    
     
    def __str__(self):
        return self.department

from django.db import models
from Standup.manager import CustomManager
# Create your models here.
class Books(models.Model):
    Bname=models.CharField(max_length=70)
    Bauthor=models.CharField(max_length=70)
    YearofPub=models.DateField()
    Price=models.FloatField()
    Page=models.IntegerField()
    Category=models.CharField(max_length=40,default="Reference")
    is_deleted=models.CharField(max_length=2,default='n')

    CustomManager=CustomManager()

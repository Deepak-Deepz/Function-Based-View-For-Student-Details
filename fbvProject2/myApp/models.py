from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length = 50)
    sdob = models.DateField()
    smarks = models.FloatField()
    sphone = models.CharField(max_length =10)
    saddr = models.CharField(max_length = 100)

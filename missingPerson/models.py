from django.db import models

# Create your models here.
from django.utils import timezone


class missingPersonInfo(models.Model):
    firstName = models.CharField(max_length=50,default='null')
    lastname = models.CharField(max_length=50,default='null')
    age = models.IntegerField(default='null')
    gender = models.TextField(default='null')
    color = models.CharField(max_length=50,default='null')
    height = models.CharField(max_length=50,default='null')
    datetime = models.DateTimeField(blank=True,null=True,default=timezone.now)
    placemissing = models.CharField(max_length=50,default='null')
    police_st = models.TextField(default='null')
    desc = models.TextField(default='null')

    def __str__(self):
        return self.firstName
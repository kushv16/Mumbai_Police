from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class missingPersonInfo(models.Model):
    admin_status = (
        ('under scrutiny', 'Under Scrutiny'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50,default='null')
    lastname = models.CharField(max_length=50,default='null')
    age = models.IntegerField(default='null')
    gender = models.TextField(default='null')
    color = models.CharField(max_length=50,default='null')
    height = models.CharField(max_length=50,default='null')
    datetime = models.DateField(blank=True,null=True,default=timezone.now)
    placemissing = models.CharField(max_length=50,default='null')
    police_st = models.TextField(default='null')
    desc = models.TextField(default='null')
    image = models.ImageField(default='default.png',upload_to='missing_person_pics')

    def __str__(self):
        return self.firstName + " " + self.lastname
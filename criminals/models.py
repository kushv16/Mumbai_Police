from django.db import models

# Create your models here.
from django.utils import timezone


class criminalsInfo(models.Model):
    fullName = models.CharField(max_length=50,default='null')
    lastname = models.CharField(max_length=50,default='null')
    age = models.IntegerField(default='null')
    gender = models.TextField(default='null')
    address = models.TextField(default='null')
    pincode = models.IntegerField(default='null')
    prison_sentence = models.IntegerField(default='null')
    crime = models.TextField(default='null')
    current_status = models.TextField(default='null')
    datetime = models.DateTimeField(blank=True,null=True,default=timezone.now)
    desc = models.TextField(default='null')
    image = models.ImageField(default='default.jpg',upload_to='criminal_pics')


    def __str__(self):
        return self.fullName



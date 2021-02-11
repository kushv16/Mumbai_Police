
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class complaintsInfo(models.Model):
    fullName = models.CharField(max_length=50)
    contact = models.CharField(max_length=30)
    email = models.EmailField()
    flatno = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    datetime = models.DateTimeField(blank=True,null=True,default=timezone.now)
    crime = models.TextField()
    desc = models.TextField()

    def __str__(self):
        return self.fullName

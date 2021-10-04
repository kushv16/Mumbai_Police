
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class complaintsInfo(models.Model):
    CRIMES = (
        ('cyber', 'Cyber'),
        ('extortion', 'Extortion'),
        ('chain snatching', 'Chain Snatching'),
        ('dacotiy', 'Dacoity'),
        ('theft', 'Theft'),
        ('others', 'Others'),
    )
    fullName = models.CharField(max_length=50,default='null')
    contact = models.CharField(max_length=30,default='null')
    email = models.EmailField(default='null')
    flatno = models.CharField(max_length=50,default='null')
    address = models.CharField(max_length=50,default='null')
    city = models.CharField(max_length=50,default='null')
    state = models.CharField(max_length=50,default='null')
    country = models.CharField(max_length=50,default='null')
    datetime = models.DateTimeField(blank=True,null=True,default=timezone.now)
    crime = models.CharField(max_length=50, choices=CRIMES,default='null')
    desc = models.CharField(max_length=250,default='null')

    def __str__(self):
        return self.fullName

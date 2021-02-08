from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Complaint:
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    type = models.TextField()
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='pics')
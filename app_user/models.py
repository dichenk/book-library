from django.db import models
from django.utils import timezone
# from config import settings


class Customer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

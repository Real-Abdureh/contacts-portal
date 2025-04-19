from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=20)
    

    REQUIRED_FIELDS = ['full_name', 'contact_number']

from django.db import models
from userauths.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.user.username}"

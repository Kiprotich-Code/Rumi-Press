from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_names = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='staff')
    date_joined = models.DateField()

    def __str__(self):
        return self.full_names
from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=25, blank=True)
    date_born = models.DateField(blank=True)
    interests = models.CharField(max_length=255, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.name

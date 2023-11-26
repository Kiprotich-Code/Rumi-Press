from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=25, blank=True)
    date_born = models.DateTimeField()
    date_died = models.DateTimeField(blank=True)
    interests = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

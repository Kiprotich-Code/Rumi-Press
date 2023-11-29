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
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    additional_info = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.name
    

class Publisher(models.Model):
    pub_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=250, blank= True)

    def __str__(self):
        return self.pub_name


class Books(models.Model):
    book_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=55)
    subtitle = models.CharField(max_length=55)
    authors = models.ManyToManyField(Authors, blank=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    published_date = models.DateField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.title} by {self.authors}'


class Expense(models.Model):
    book = models.ForeignKey(Books, to_field= 'book_id',on_delete=models.CASCADE)
    distribution_date = models.DateField()
    distribution_expense = models.FloatField()
    confirmed_by = models.CharField(max_length=100)

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# Country model
class Country(models.Model):

    name = models.CharField(max_length=100)
    officialname = models.CharField(max_length=200)
    capital = models.CharField(max_length=200)
    flag = models.TextField(max_length=900)
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=30)
    region = models.CharField(max_length=100)
    population = models.CharField(max_length=200)
    
    

    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'country_id': self.id})
  


# Bucket model
class Bucket(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.TextField(max_length=500)
    budget = models.CharField(max_length=30)
    description = models.TextField(max_length=400)

    # Create a country_id FK
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'bucket_id': self.id})
  




# Review model
class Review(models.Model):
    description = models.TextField(max_length=400)
    # Create a bucket_id FK
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'review_id': self.id})
  

   






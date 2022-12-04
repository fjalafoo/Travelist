from django.db import models

# Create your models here.

# Country model
class Country(models.Model):
    name = models.CharField(max_length=100)
    flag = models.TextField(max_length=500)
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=30)


# Bucket model
class Bucket(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.TextField(max_length=500)
    budget = models.CharField(max_length=30)
    description = models.TextField(max_length=400)



# Review model
class Review(models.Model):
    description = models.TextField(max_length=400)





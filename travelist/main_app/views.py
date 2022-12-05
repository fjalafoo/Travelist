from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Country, Bucket, Review

import requests
import json

# c = requests.get('https://restcountries.com/v3.1/all')
# bahrain = requests.get('https://restcountries.com/v3.1/name/bahrain')

# data = bahrain.text
# json.loads(data)


# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')


# Define the about view
def about(request):
  return render(request, 'about.html')


# Define the travel tips view
def tips(request):
  return render(request, 'tips.html')


# Define the contact view
def contact(request):
  return render(request, 'contact.html')



# Define the country details view
def countries_details(request):
  bahrain = requests.get('https://restcountries.com/v3.1/name/bahrain')
  c = requests.get('https://restcountries.com/v3.1/all')
  print(list(bahrain.json()))
  return render(request, 'countries/details.html', { 'bahrian': bahrain.json(), 'c': c.json() })
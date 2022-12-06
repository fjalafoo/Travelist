from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Country, Bucket, Review
from django.contrib.auth import login
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

import requests
import json

# c = requests.get('https://restcountries.com/v3.1/all')
# bahrain = requests.get('https://restcountries.com/v3.1/name/bahrain')

# data = bahrain.text
# json.loads(data)


# Create your views here.

def signup(request):
  error_message = ''
  if request.method == 'POST':
    
    form = UserCreationForm(request.POST)
    if form.is_valid():
    
      user = form.save()
     
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
 
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

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



#Define the country details view
def countries_details(request):
  return render(request, 'countries/details.html')

# Define the country index view
def countries_index(request):
  bahrain = requests.get('https://restcountries.com/v3.1/name/bahrain')
  c = requests.get('https://restcountries.com/v3.1/all')
  print(list(bahrain.json()))
  return render(request, 'countries/index.html', { 'bahrian': bahrain.json(), 'c': c.json() })
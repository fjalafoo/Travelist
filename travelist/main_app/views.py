from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Country, Bucket, Review
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


import requests
import json

# c = requests.get('https://restcountries.com/v3.1/all')
# bahrain = requests.get('https://restcountries.com/v3.1/name/bahrain')



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


class CountryCreate(LoginRequiredMixin, CreateView):
  model = Country
  fields = ['name', 'officialname', 'capital', 'flag', 'language', 'currency', 'region', 'population']
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)


class CountryUpdate(UpdateView):
  model = Country
  fields = ['language', 'currency', 'population']

class CountryDelete(DeleteView):
  model = Country
  success_url = '/countries/'




# Define the home view
def home(request):
  return render(request, 'home.html')

# Define the thanks view
def thanks(request):
  return render(request, 'thanks.html')

# Define the about view
def about(request):
  return render(request, 'about.html')


# Define the travel tips view
def tips(request):
  return render(request, 'tips.html')


# Define the contact view
def contact(request):
  return render(request, 'contact.html')



# # Define the country index view
# def countries_index(request):
#   # c = requests.get('https://restcountries.com/v3.1/all')
#   # return render(request, 'countries/index.html', { 'c': c.json() })
#   return render(request, 'countries/index.html', { 'countrys': countrys })



@login_required
def countries_index(request):
  countrys = Country.objects.filter(user=request.user)
  return render(request, 'countries/index.html', { 'countrys': countrys })





#Define the country details view
def countries_details(request, country_id):
  country = Country.objects.get(id=country_id)
  return render(request, 'countries/details.html', { 'country': country})


def buckets_index(request):
  buckets = Bucket.objects.filter(country_id=country_id)
  return render(request, 'buckets/bindex.html', { 'buckets': buckets })

#Define the bucket details view
def buckets_details(request, bucket_id):
  buckets = Bucket.objects.get(id=bucket_id)
  return render(request, 'buckets/bdetails.html', { 'buckets': buckets })


class BucketCreate(CreateView):
  model = Bucket
  fields = '__all__'

  def form_valid(self, form):
    form.instance.country = self.request.country  
    return super().form_valid(form)


class BucketUpdate(UpdateView):
  model = Bucket
  fields = '__all__'

class BucketDelete(DeleteView):
  model = Bucket
  success_url = '/buckets/'


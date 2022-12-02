from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3

# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')


# Define the about view
def about(request):
  return render(request, 'about.html')

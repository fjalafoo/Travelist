from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tips/', views.tips, name='tips'),
  path('contact/', views.contact, name='contact'),
  path('countries/', views.countries_details, name='details')
 
]
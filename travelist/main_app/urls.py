from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tips/', views.tips, name='tips'),
  path('contact/', views.contact, name='contact'),

  path('countries/', views.countries_index, name='countries'),
  path('countries/<int:country_id>/', views.countries_details, name='details'),
  path('countries/create/', views.CountryCreate.as_view(), name='countries_create'),
  path('countries/<int:pk>/update/', views.CountryUpdate.as_view(), name='countries_update'),
  path('countries/<int:pk>/delete/', views.CountryDelete.as_view(), name='countries_delete'),
  
  path('buckets/', views.buckets_index, name='buckets'),
  path('buckets/<int:bucket_id>/', views.buckets_details, name='bdetails'),
  path('buckets/create/', views.BucketCreate.as_view(), name='buckets_create'),
  path('buckets/<int:pk>/update/', views.BucketUpdate.as_view(), name='buckets_update'),
  path('buckets/<int:pk>/delete/', views.BucketDelete.as_view(), name='buckets_delete'),

  path('thanks/', views.thanks, name='thanks'),
  path('accounts/signup/', views.signup, name='signup'),

 
]
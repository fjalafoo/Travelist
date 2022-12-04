from django.contrib import admin
from .models import Country
from .models import Bucket
from .models import Review


# Register your models here.
admin.site.register(Country)
admin.site.register(Bucket)
admin.site.register(Review)

from django.contrib import admin
from .models import FoodCard, FoodCategory

# Register your models here.
admin.site.register(FoodCard)
admin.site.register(FoodCategory)
from django.contrib import admin
from .models import Category, Product, Bill
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Bill)

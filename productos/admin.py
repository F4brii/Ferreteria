from django.contrib import admin
from .models import Category, Product, Bill, Detail
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Detail)

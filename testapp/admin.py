from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','description','category','image']
admin.site.register(Product,ProductAdmin)


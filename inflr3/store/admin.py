from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','created_at']
    search_fields = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
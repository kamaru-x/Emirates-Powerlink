from django.contrib import admin
from Core.models import Category,Sub_Category,Sub_In_Category,Product

# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Reference','Note','Added_Date','Added_By']

@admin.register(Sub_Category)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Category','Reference','Note']

@admin.register(Sub_In_Category)
class SubInCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Sub_Category','Reference','Note']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Reference','Note','Added_Date','Added_By']
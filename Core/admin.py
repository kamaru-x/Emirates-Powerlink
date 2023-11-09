from django.contrib import admin
from Core.models import Category

# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Reference','Note','Added_Date','Added_By']
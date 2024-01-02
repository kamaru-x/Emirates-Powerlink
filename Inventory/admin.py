from django.contrib import admin
from Inventory.models import InventoryItem,Inventory_Out,Inventory_Category,Inventory_In

# Register your models here.

@admin.register(Inventory_Category)
class InventoryCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Date']

@admin.register(InventoryItem)
class InventoryItemModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Quantity']

@admin.register(Inventory_Out)
class InventoryOutModelAdmin(admin.ModelAdmin):
    list_display = ['Project','Date','Item','Quantity']

@admin.register(Inventory_In)
class InventoryInModelAdmin(admin.ModelAdmin):
    list_display = ['Item','Date','Quantity']
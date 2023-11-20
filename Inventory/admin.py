from django.contrib import admin
from Inventory.models import Inventory,InventoryItem

# Register your models here.

@admin.register(Inventory)
class InventoryModelAdmin(admin.ModelAdmin):
    list_display = ['Reference','Project']

@admin.register(InventoryItem)
class InventoryItemModelAdmin(admin.ModelAdmin):
    list_display = ['Inventory','Item']
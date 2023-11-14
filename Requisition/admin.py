from django.contrib import admin
from Requisition.models import Requisition,Requisition_Item

# Register your models here.

@admin.register(Requisition)
class RequisitionModelAdmin(admin.ModelAdmin):
    list_display = ['Reference','Project','Added_By']

@admin.register(Requisition_Item)
class Requisition_ItemModelAdmin(admin.ModelAdmin):
    list_display = ['Requisition','Product','Quantity','Note']
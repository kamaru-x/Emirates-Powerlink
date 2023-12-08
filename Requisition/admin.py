from django.contrib import admin
from Requisition.models import Requisition,Requisition_Item,Service,Service_Attachment

# Register your models here.

@admin.register(Requisition)
class RequisitionModelAdmin(admin.ModelAdmin):
    list_display = ['Reference','Project','Added_By','Requisition_Status']

@admin.register(Requisition_Item)
class Requisition_ItemModelAdmin(admin.ModelAdmin):
    list_display = ['Requisition','Product','Quantity','Note']

@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['Requisition','Title']

@admin.register(Service_Attachment)
class AttachmentModelAdmin(admin.ModelAdmin):
    list_display = ['Service']
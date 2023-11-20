from django.contrib import admin
from Quotation.models import Quotation,QuotationItem,LPO

# Register your models here.

@admin.register(Quotation)
class QuotationModelAdmin(admin.ModelAdmin):
    list_display = ['Reference','Requisition','Vendor','Date','Status','Sub_Total']

@admin.register(QuotationItem)
class QuotationItemModelAdmin(admin.ModelAdmin):
    list_display = ['Quotation','Item']

@admin.register(LPO)
class LPOModelAdmin(admin.ModelAdmin):
    list_display = ['Quotation','Reference']
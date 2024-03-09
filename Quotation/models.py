from django.db import models
from Requisition.models import Requisition,Requisition_Item
from U_Auth.models import User
# Create your models here.

class Quotation(models.Model):
    Status = models.IntegerField(default=1) # 0 rejected , 1 pending , 2 selected , 3 converted to lpo
    Date = models.DateField(auto_now_add=True)
    LPO_Date = models.DateField(null=True)
    Reference = models.CharField(max_length=25)
    Note = models.CharField(max_length=255,null=True)
    
    Requisition = models.ForeignKey(Requisition,on_delete=models.SET_NULL,null=True)
    Vendor = models.CharField(max_length=100)
    Sub_Total = models.FloatField(default=0)

    Approved_By = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.Requisition.Reference}-{self.Vendor}'
    
class QuotationItem(models.Model):
    Quotation = models.ForeignKey(Quotation, related_name='items', on_delete=models.CASCADE)
    Item = models.ForeignKey(Requisition_Item,on_delete=models.CASCADE)

    Brand = models.CharField(max_length=100,null=True)
    Price = models.FloatField(default=0,null=True)
    Net = models.FloatField(default=0,null=True)

    def __str__(self):
        return f'{self.Quotation}-{self.Item}'
    
class LPO(models.Model):
    Quotation = models.ForeignKey(Quotation,on_delete=models.CASCADE)
    PO_NO = models.CharField(max_length=50,null=True)

    TRN = models.CharField(max_length=25,null=True)
    PO_Date = models.DateField(null=True)
    PO_Category = models.CharField(max_length=100,null=True)
    Q_Reference = models.CharField(max_length=25,null=True)
    Reference = models.CharField(max_length=50,null=True)
    Address = models.CharField(max_length=255,null=True)
    Telephone = models.CharField(max_length=25,null=True)
    Email = models.EmailField(null=True)
    Mobile = models.CharField(max_length=25,null=True)
    
    Payment_Terms = models.TextField(null=True)
    Delivery_Terms = models.TextField(null=True)
    Terms_Condetions = models.TextField(null=True)

    Contact = models.CharField(max_length=50,null=True)
    Delivery_Location = models.CharField(max_length=50,null=True)
    Remarks = models.CharField(max_length=255,null=True)

    Payment_Mode = models.CharField(max_length=50,null=True)
    Delivery_Date = models.DateField(null=True)
    Order_Date = models.DateField(null=True)

    # def __str__(self):
    #     return self.Reference
from django.db import models
from Projects.models import Project
from U_Auth.models import User
from Quotation.models import QuotationItem

# Create your models here.

class Inventory_Category(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name =models.CharField(max_length=100)

    def __str__(self):
        return self.Name
    
class InventoryItem(models.Model):
    Category = models.ForeignKey(Inventory_Category,on_delete=models.CASCADE)
    Reference = models.CharField(max_length=50)
    Name = models.CharField(max_length=100)
    Quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.Name

class Inventory_In(models.Model):
    Date = models.DateField(auto_now_add=True)
    Item = models.ForeignKey(InventoryItem,on_delete=models.CASCADE)
    Quantity = models.IntegerField()

    def __str__(self):
        return self.Item
    
class Inventory_Out(models.Model):
    Date = models.DateField(auto_now_add=True)
    Project = models.ForeignKey(Project,on_delete=models.DO_NOTHING)
    Item = models.ForeignKey(InventoryItem,on_delete=models.DO_NOTHING)
    Quantity = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.Item
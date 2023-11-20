from django.db import models
from Projects.models import Project
from U_Auth.models import User
from Quotation.models import QuotationItem

# Create your models here.

class Inventory(models.Model):
    Project = models.ForeignKey(Project,on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=True)
    Added_By = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    Reference = models.CharField(max_length=25)

    def __str__(self):
        return self.Reference
    
class InventoryItem(models.Model):
    Inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE)
    Item = models.ForeignKey(QuotationItem,on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.Inventory.Reference
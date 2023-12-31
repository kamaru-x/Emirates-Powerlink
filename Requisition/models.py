from django.db import models
from U_Auth.models import User
from Projects.models import Project
from Core.models import Product

# Create your models here.

class Requisition(models.Model):
    Status = models.IntegerField(default=1)
    Requisition_Status = models.CharField(default='PENDING',max_length=50) # 1 Peding,
    Requisition_Type = models.IntegerField(default=1) # 1 material requisition , 2 service requisition
    Reference = models.CharField(max_length=50)

    Added_By = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='requisition_created')
    Added_Date = models.DateField(auto_now_add=True)
    Added_IP = models.GenericIPAddressField(null=True)

    Edited_By = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='requisition_edited')
    Edited_Date = models.DateField(null=True)
    Edited_IP = models.GenericIPAddressField(null=True)

    Project = models.ForeignKey(Project,on_delete=models.DO_NOTHING)

    Prepared_By = models.ForeignKey(User,related_name='prepared_by',on_delete=models.SET_NULL,null=True)
    Checked_By = models.ForeignKey(User,related_name='checked_by',on_delete=models.SET_NULL,null=True)
    Approved_By = models.ForeignKey(User,related_name='approved_by',on_delete=models.SET_NULL,null=True)

    Rejected_By = models.ForeignKey(User,related_name='rejected_by',on_delete=models.SET_NULL,null=True)
    Reason = models.TextField(null=True)

    def __str__(self):
        return self.Reference
    
class Requisition_Item(models.Model):
    Requisition = models.ForeignKey(Requisition,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    Quantity = models.IntegerField(default=0)
    Note = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f'{self.Requisition}-{self.Product}'
    
class Service(models.Model):
    Requisition = models.ForeignKey(Requisition,on_delete=models.CASCADE)
    Title = models.CharField(max_length=225,null=True)
    Description = models.TextField(null=True)

    def __str__(self):
        return self.Title
    
class Service_Attachment(models.Model):
    Service = models.ForeignKey(Service,on_delete=models.CASCADE)
    Attachment = models.FileField(upload_to='service',null=True)

    def __str__(self):
        return self.Service.Title
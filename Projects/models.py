from django.db import models
from U_Auth.models import User

# Create your models here.

class Project(models.Model):
    Status = models.IntegerField(default=1)
    Project_Status = models.IntegerField(default=0) # 0 project created ,
    Reference = models.CharField(max_length=50)

    Added_By = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='project_created')
    Added_Date = models.DateField(auto_now_add=True)
    Added_IP = models.GenericIPAddressField(null=True)

    Edited_By = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='project_edited')
    Edited_Date = models.DateField(null=True)
    Edited_IP = models.GenericIPAddressField(null=True)

    Project_Name = models.CharField(max_length=100)
    project_Description = models.TextField(null=True)
    
    Client_Name = models.CharField(max_length=100)
    Client_Mobile = models.CharField(max_length=15,null=True)
    Client_Email = models.EmailField(null=True)
    Client_Address = models.TextField(null=True)

    Contact_Name = models.CharField(max_length=100,null=True)
    Contact_Number = models.CharField(max_length=15,null=True)
    
    Expected_Starting_Date = models.DateField(null=True)
    Expected_Amount = models.FloatField(null=True)

    Department_Managers = models.ManyToManyField(User,related_name='Department_Managers')
    Project_Engineers = models.ManyToManyField(User,related_name='Project_Engineers')
    Purchase_Managers = models.ManyToManyField(User,related_name='Purchase_Managers')
    Site_Engineers = models.ManyToManyField(User,related_name='Site_Engineers')

    def __str__(self):
        return self.Client_Name
from django.db import models
from U_Auth.models import User

# Create your models here.

class Category(models.Model):
    Status = models.IntegerField(default=1)

    Added_By = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='category_added')
    Added_Date = models.DateField(auto_now_add=True)
    Added_IP = models.GenericIPAddressField(null=True)

    Edited_By = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='category_edited')
    Edited_Date = models.DateField(null=True)
    Edited_IP = models.GenericIPAddressField(null=True)

    Name = models.CharField(max_length=100,unique=True)
    Reference = models.CharField(max_length=25,unique=True)
    Note = models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.Name
    
class Sub_Category(models.Model):
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='sub_category')
    Name = models.CharField(max_length=100,unique=True)
    Reference = models.CharField(max_length=25,unique=True)
    Note = models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.Name
    
class Sub_In_Category(models.Model):
    Sub_Category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100,unique=True)
    Reference = models.CharField(max_length=25,unique=True)
    Note = models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.Name
    
class Product(models.Model):
    Status = models.IntegerField(default=1)

    Added_By = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='product_added')
    Added_Date = models.DateField(auto_now_add=True)
    Added_IP = models.GenericIPAddressField(null=True)

    Name = models.CharField(max_length=100,unique=True)
    Reference = models.CharField(max_length=25,unique=True)

    Category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='product')
    Sub_Category = models.ForeignKey(Sub_Category,on_delete=models.SET_NULL,null=True)
    Sub_In_Category = models.ForeignKey(Sub_In_Category,on_delete=models.SET_NULL,null=True)

    Unit = models.CharField(max_length=100)
    Note = models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.Name
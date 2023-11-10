from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

JOBROLES = [
        ('Department Manager', 'Department Manager'),
        ('Project Engineer', 'Project Engineer'),
        ('Purchase Manager', 'Purchase Manager'),
        ('Site Engineer', 'Site Engineer'),
        ('Accountant', 'Accountant'),
    ]

class User(AbstractUser):
    Image = models.ImageField(null=True,upload_to='Team')
    Staff_ID = models.CharField(max_length=25,null=True)
    Mobile = models.CharField(max_length=20,null=True)
    Job_Role = models.CharField(max_length=25,choices=JOBROLES,null=True)

    def __str__(self):
        return self.first_name
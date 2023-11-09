from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    Image = models.ImageField(null=True,upload_to='Team')
    Staff_ID = models.CharField(max_length=25)
    Mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
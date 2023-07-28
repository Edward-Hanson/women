from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    GENDER_CHOICES =(
        ('M','Male'),
        ('F','Female'),
    )
    age= models.PositiveIntegerField(blank=True, null=True,default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username
from django.db import models

# Create your models here.
class Profs(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=25,blank=True, null=True)
    occupation =models.CharField(max_length=25)
    institution= models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to= 'media')
    telephone= models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
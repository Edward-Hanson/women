from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Job(models.Model):
    author= models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    certificate = models.FileField(upload_to='media', validators= [FileExtensionValidator(allowed_extensions=['pdf'])])
    ghana_card = models.CharField(max_length=15)
    confirm_job= models.BooleanField(default= False)
    date = models.DateTimeField(default= timezone.now)
    telephone = models.PositiveIntegerField()
    company = models.CharField(max_length=25)
    
    def validate_ghana_card(self):
        card = str(self.ghana_card)
        if len(card) != 15 or not card.startswith("GHA-") or card[13] != "-":
            raise ValidationError("Invalid Ghana-Card")
    
    def clean(self):
        super().clean()  
        self.validate_ghana_card() 
        
    def job_confirm(self):
        self.confirm_job = True
        self.save()
        
    def __str__(self):
        return self.title
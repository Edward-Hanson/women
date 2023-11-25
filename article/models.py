from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    title = models.CharField(max_length=50)
    body = RichTextField()
    image = models.ImageField(upload_to= 'media')
    published_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
    
    
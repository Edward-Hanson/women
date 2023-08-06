from django.contrib import admin
from .models import Job

# Register your models here.
class CustomJob(admin.ModelAdmin):
    list_display = ('title','author','confirm_job','telephone','company',)
    ordering = ('-date',)
    search_fields = ('title',)
    
admin.site.register(Job,CustomJob)
from django.contrib import admin
from .models import Profs

# Register your models here.
class ProfAdmin(admin.ModelAdmin):
    list_display = ('occupation','institution',)
    
admin.site.register(Profs,ProfAdmin)
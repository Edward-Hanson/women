from django.contrib import admin
from .models import FilesAdmin

class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','downloadcount',)
    list_filter =  ('downloadcount',)
    search_fields = ('title', 'description')

admin.site.register(FilesAdmin, FileAdmin)
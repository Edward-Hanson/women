from django.contrib import admin

from .models import Article

# Register your models here
class CustomArticle(admin.ModelAdmin):
    list_display = ('title','author',)
    ordering = ('-published_date',)
    search_fields = ('title',)
    
admin.site.register(Article,CustomArticle)
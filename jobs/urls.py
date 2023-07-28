from django.urls import path

from .views import create_job, list_job


urlpatterns = [
    path('create_jobs/',create_job, name='create_job'),
    path('',list_job,name='list_job'),
    
]
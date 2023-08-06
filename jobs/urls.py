from django.urls import path

from .views import create_job, list_job, delete_job, pending_list, detailed_job


urlpatterns = [
    path('create_jobs/',create_job, name='create_job'),
    path('',list_job,name='list_job'),
    path('delete/<int:pk>/',delete_job,name='delete_job'),
    path('pending/',pending_list,name='pending_list'),
    path('detail/<int:pk>/',detailed_job,name='detailed_job'),
]
from django.urls import path
from .views import create_profs, del_prof, list_profs, detail_prof,search_prof

urlpatterns  = [
    path('create_prof',create_profs,name='create_prof'),
    path('del/<int:pk>/',del_prof,name ='del_prof'),
    path('list_profs/',list_profs,name= 'list_profs'),
    path('detail/<int:pk>',detail_prof, name= 'detail_prof'),
    path('search/',search_prof,name='search_prof'),
]
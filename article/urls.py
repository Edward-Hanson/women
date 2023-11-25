from django.urls import path

from .views import article_list, article_edit, article_delete,article_detail,article_create

app_name = 'article'


urlpatterns = [
    path('',article_list,name='list'),
    path('new/',article_create,name='create'),
    path('details/<int:pk>/',article_detail,name='detail'),
    path('del/<int:pk>/',article_delete,name='delete'),
    path('edit/<int:pk>/',article_edit,name='edit'),
    
]
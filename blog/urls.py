from django.urls import path
from .views import listfiles, download, query_set, send_email,detailfile,upload, delete_post

urlpatterns = [
    path('',listfiles,name='list'),
    path('<slug:cat>/',listfiles,name='list_by_cat'),
    path('detail/<int:pk>/',detailfile, name= 'detail'),
    path('files/download/<int:file_id>/', download, name='file_download'),
    path('results',query_set,name='search_files'),
    path('blog/detail/<int:pk>/',send_email, name='share_mail'),
    path('blog/upload',upload,name='upload'),
    path('del/<int:pk>/',delete_post,name='delete_post'),

]
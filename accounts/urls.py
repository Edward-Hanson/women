from django.urls import path
from .views import signup,login, activate_account
urlpatterns = [
    path('signup/',signup,name='signup'),
    path('',login,name='login'),
    path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate_account'),
]
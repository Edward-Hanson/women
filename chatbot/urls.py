# chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.ChatMessage, name='chat'),
     path('chat/clear/', views.clear_messages, name='clear-messages'),
]

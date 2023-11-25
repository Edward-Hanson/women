from django.shortcuts import render, redirect
from .forms import ChatForm
import openai
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os

openai.api_key = os.environ.get('API_KEY')
messages = [{"role": "system", "content": "I am a Professional Expert."}]

def ChatMessage(request):
    if request.method == 'POST':
        chat_form = ChatForm(request.POST)  # Initialize the form with POST data
        
        if 'delete' in request.POST:
            messages.clear()
            
        if chat_form.is_valid():
            user_input = chat_form.cleaned_data.get('user_input')  # Use get() method to avoid AttributeError
            
            if user_input:
                messages.append({"role": "user", "content": user_input})
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )
                Chat_reply = response["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": Chat_reply})
    chat_form = ChatForm()  # Initialize an empty form for GET requests

    return render(request, "chat/chat.html", {"messages": messages, "chat_form": chat_form})

@login_required
def clear_messages(request):
    # Clear the chat messages by resetting the "messages" list
    messages.clear()
    # Redirect back to the chat interface
    return redirect('chat')
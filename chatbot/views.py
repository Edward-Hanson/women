from django.shortcuts import render, redirect
from .forms import ChatForm
import openai

openai.api_key = "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"
messages = [{"role": "system", "content": "You are a female assistant and gender expert. Ask me any questions related to gender or any other topic."}]

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
    else:
        chat_form = ChatForm()  # Initialize an empty form for GET requests

    return render(request, "chat/chat.html", {"messages": messages, "chat_form": chat_form})

def clear_messages(request):
    # Clear the chat messages by resetting the "messages" list
    messages.clear()
    # Redirect back to the chat interface
    return redirect('chat')
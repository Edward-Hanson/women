from django import forms

class ChatForm(forms.Form):
    user_input = forms.CharField(label='Your message', widget=forms.TextInput(attrs={'placeholder': 'Type your message...'}))

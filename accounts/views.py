from django.shortcuts import render,redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages

from .forms import SignupForm,LoginForm
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print('data:', form.cleaned_data)
            post= form.save(commit=False)
            post.is_active = False
            post.save()
            
            host_name= request.get_host()
            uid = urlsafe_base64_encode(force_bytes(post.id))
            token = default_token_generator.make_token(post)
            activation_link = f"{request.scheme}://{host_name}{reverse('activate_account', kwargs={'uidb64': uid, 'token': token})}"
            email_html_message = render_to_string('registration/activation_email.html', { 
                'user': post, 
                'activation_link':activation_link, 
            }) 
            # Send the activation email 
            email = EmailMessage( 
                'Account Activation', 
                email_html_message, 
                from_email='WomenWorld.com', 
                to=[post.email], 
                 
            )
            email.content_subtype = 'html'
            email.send()
            messages.info(request, 'Signup successful, kindly check your email for activation link')
            return redirect('login')          
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Account Activated. You can now login")
        return redirect('login')
    else:
        messages.error(request, "Invalid activation link")
        return redirect("login")
    
def login(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=="POST":
        form= LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user= authenticate(request,username=username,password=password)
            print(username, password)
            
            if user is not None:
                if user.is_active:
                    auth_login(request,user)
                    return redirect('home')
                messages.info(request,"Kindly check you email for the account activation link")
                return redirect('login')
            messages.error(request,'Wrong Username or Password')
            return redirect('login')
    else:
        form = LoginForm()
    return render(request,'registration/login.html',{'form':form})
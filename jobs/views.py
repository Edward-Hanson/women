from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

from .forms import JobForm
from .models import Job

# Create your views here.
def create_job(request):
    if request.method == "POST":
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if request.user.is_staff:
                post.confirm_job = True
            post.save()
            messages.info(request,"Upload Success! \n You job post will undergo Scrutiny",)
            return redirect('home')
    else:
        form= JobForm()
    return render(request,'job/create_job.html',{'form':form})

def list_job(request):
    jobs= Job.objects.filter(confirm_job=True).order_by('-date')
    return render(request,'job/list_job.html',{'jobs':jobs})

def delete_job(request,pk):
    post= get_object_or_404(Job,pk=pk)
    post.delete()
    return redirect('list_job')

def confirmed_list(request):
    confirmed_list = Job.objects.filter(confirm_job=True).order_by('-date')
    return render(request,'job/list_job.html',{'confirmed_list':confirmed_list})
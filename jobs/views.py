from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from .forms import JobForm
from .models import Job

# Create your views here.
@login_required
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
            return redirect('list_job')
    else:
        form= JobForm()
    return render(request,'job/create_job.html',{'form':form})

@login_required
def list_job(request):
    # Get all confirmed jobs and order them by date
    jobs = Job.objects.filter(confirm_job=True).order_by('-date')

    # Create a Paginator object with 16 jobs per page
    paginator = Paginator(jobs, 16)

    # Get the page number from the request's GET parameters (default to 1)
    page_number = request.GET.get('page', 1)

    # Get the Page object for the requested page number
    page = paginator.get_page(page_number)

    return render(request, 'job/list_job.html', {'page': page})

@staff_member_required
@login_required
def delete_job(request,pk):
    post= get_object_or_404(Job,pk=pk)
    post.delete()
    return redirect('list_job')


@login_required
def confirmed_list(request):
    confirmed_list = Job.objects.filter(confirm_job=True).order_by('-date')
    return render(request,'job/list_job.html',{'confirmed_list':confirmed_list})

@staff_member_required
@login_required
def pending_list(request):
    pending_list = Job.objects.filter(confirm_job= False).order_by('-date')
    return render(request,'job/pending_list.html',{'pending_list': pending_list})

@login_required
def detailed_job(request,pk):
    job = get_object_or_404(Job,pk=pk)
    return render(request,'job/detailed_job.html',{'job':job})

@login_required
def download(request,pk):
    file = get_object_or_404(Job,pk=pk)
    return redirect(file.certificate.url)

@staff_member_required
@login_required
def confirm_job(request,pk):
    job= get_object_or_404(Job,pk=pk)
    job.job_confirm()
    return redirect('detailed_job',pk=pk)

@login_required
def search_list(request):
    word = request.GET.get('search')
    if not word:
        return redirect('list_job')
    jobs= Job.objects.filter(Q(title__icontains=word)| Q(description__icontains=word))
    return render(request,'job/search_list.html',{'jobs':jobs,'word':word})
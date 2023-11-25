from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View
from .models import FilesAdmin
import os
from django.db.models import Q
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from .forms import EmailForm,UploadForm
from django.shortcuts import redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
@login_required
def listfiles(request,cat=None):
    files = FilesAdmin.objects.all()
    paginator = Paginator(files, 16)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    if cat:
        files_by_cat =[]
        for file in files:
            if file.get_file_type()==cat:
                files_by_cat.append(file)
                paginator = Paginator(files_by_cat, 16)
                page_number = request.GET.get('page', 1)
                page = paginator.get_page(page_number)

        return render(request,'blog/list.html',{'files':page})
                
   
    return render(request,'blog/list.html',{'files':page})

@login_required
def detailfile(request,pk):
    file= get_object_or_404(FilesAdmin,pk=pk)
    return render(request,'blog/detail.html',{'file':file})

@login_required
def download(request, file_id):
    file_obj = get_object_or_404(FilesAdmin, pk=file_id)
    file_obj.downloadcount += 1
    file_obj.save()
    return redirect(file_obj.adminupload.url)
    
@login_required   
def query_set(request):
    word = request.GET.get('q')
    print("word:" ,word)
    results = FilesAdmin.objects.filter(Q(title__icontains=word)  | Q(description__icontains=word))
    print(results)
    return render(request,'blog/search_results.html', {'files':results})

@staff_member_required
@login_required
def upload(request):
    if request.method=="POST":
        form= UploadForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.save()
            messages.info(request,"Upload Success")
            return redirect('detail', pk=file.pk)
    else:
        form= UploadForm()
    return render(request,'blog/upload.html',{'form':form})


@login_required 
def send_email(request, pk):
    user = request.user
    default_active_file = get_object_or_404(FilesAdmin, pk=pk)
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_email']

            email = EmailMessage(
                subject='File Attachment',
                body='Please find the attached file',
                from_email=user.email,
                to=[recipient_email],
            )
            email.attach_file(default_active_file.adminupload.path)
            email.send()

            messages.info(request, 'Email sent successfully!')
            return redirect('detail',pk=default_active_file.pk)
    else:
        form = EmailForm()

    context = {'form': form}
    return render(request, 'blog/email_form.html', context)

@staff_member_required
@login_required
def delete_post(request,pk):
    post= get_object_or_404(FilesAdmin,pk=pk)
    post.delete()
    return redirect('list')


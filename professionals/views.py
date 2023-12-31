from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


from .forms import ProfForm
from .models import Profs


# Create your views here.
@staff_member_required
@login_required
def create_profs(request):
    if request.method == "POST":
        form = ProfForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.info(request,'Profile successfully Created :) ')
            return redirect('list_profs')
    else:
        form = ProfForm()
    return render(request,'prof/create_prof.html',{'form':form})

@staff_member_required
@login_required
def del_prof(request,pk):
    prof = get_object_or_404(Profs,pk=pk)
    prof.delete()
    return redirect('list_profs')

@login_required
def list_profs(request):
    profs = Profs.objects.all()
    return render(request,'prof/list_profs.html',{'profs':profs})

@login_required
def detail_prof(request,pk):
    prof = get_object_or_404(Profs,pk=pk)
    return render(request,'prof/detail_prof.html',{'prof':prof})

@login_required
def search_prof(request):
    word = request.GET.get('search')
    if not word:
        return redirect('list_profs')
    profs= Profs.objects.filter(Q(occupation__icontains=word)| Q(name__icontains=word))
    return render(request,'prof/search_list.html',{'profs':profs})
        
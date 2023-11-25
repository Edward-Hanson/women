from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



from .models import Article
from .forms import Article_Form

# Create your views here.
@login_required
def article_list(request):
    articles = Article.objects.all()
    articles_per_page = 9
    paginator = Paginator(articles, articles_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    return render(request, 'article/list.html', {"page": page})

@login_required
def article_detail(request,pk):
    article =get_object_or_404(Article,pk=pk)
    return render(request,'article/detail.html',{'article':article})
 
@staff_member_required
@login_required   
def article_edit(request,pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        form = Article_Form(request.POST,request.FILES, instance=article)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('article:detail', pk=post.pk)
    else:
       form = Article_Form(instance=article)
    return render(request, 'article/update.html', {'form': form})

@staff_member_required
@login_required  
def article_delete(request,pk):
    article= get_object_or_404(Article,pk=pk)
    article.delete()
    return redirect('article:list')

@staff_member_required
@login_required   
def article_create(request):
    if request.method == "POST":
        form= Article_Form(request.POST,request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # return redirect('detail',post.pk)
            return redirect('article:list')
    else:
        form = Article_Form()
    return render(request,'article/create.html',{'form':form})
            

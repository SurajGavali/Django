from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def article_home(request):
    articles = Article.objects.all().order_by("date")
    return render(request,"articles/articles.html",{'articles' : articles})

def article_detail(request,slug):
    #return HttpResponse(slug)

    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):

    
    if request.method == 'POST':
        create_article = forms.CreateArticle(request.POST,request.FILES)
        if create_article.is_valid():
            #save article to db
            current_user = create_article.save(commit=False)
            current_user.author = request.user
            current_user.save()
            return redirect('articles:home')

    else:
        create_article = forms.CreateArticle()
    return render(request,'articles/article_create.html',{'create_article':create_article})
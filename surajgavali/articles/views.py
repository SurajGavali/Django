from django.shortcuts import render

# Create your views here.

def article_home(request):
    return render(request,"articles/articles.html")
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from . models import Article

def home(request):
    articles = Article.objects.all()
    context = {'articles': articles}

    return render(request, 'lynx/index.html', context=context)



def singular_article(request, pk):

    article  = Article.objects.get(id=pk)
    context = {'article':article}
    return render(request, 'lynx/article.html', context=context)
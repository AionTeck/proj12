from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *



def mainPage(request):
    return render(request, 'news/index.html', {'title': 'Main page'})

def about(request):
    return render(request, 'news/about.html', {'title': 'About'})


def list_news(request):
    posts = News.objects.all()
    return render(request, 'news/list_news.html', {'title': 'News', 'posts': posts})


def categories(request, categories_id):
    return HttpResponse(f"<h1>Category</h1><p>{categories_id}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

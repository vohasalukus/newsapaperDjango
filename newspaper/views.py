from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def main_page(request):
    posts = Article.objects.all()
    return render(request, 'main_page.html', {'posts': posts})

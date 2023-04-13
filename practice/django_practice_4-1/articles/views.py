from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    article_list = Article.objects.all()
    context = {
        'article_list':article_list
    }
    return render(request,'articles/index.html', context)

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article()
        article.title = title
        article.content = content
        article.save()

        return redirect('articles:create')
    else:
        return render(request, 'articles/new.html')
    
def create(request):
    return render(request, 'articles/create.html')
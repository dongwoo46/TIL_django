from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # 새롭게 form만들어서 하는 것이기 때문에 새로 article을 save해야함
            article = form.save()
            return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm()
        context = {'form':form}
        return render(request, 'articles/create.html',context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    # 특정 키에 해당하는 페이지 가지고 옴
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            # 기존에 것을 변경하는 것이기 때문에 article = form.save() 불필요
            form.save()
            return redirect('articles:detail', pk=article.pk)

        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        
    else:
        form = ArticleForm(instance=article)
    context = {'form':form, 'article':article}
    return render(request, 'articles/update.html', context)

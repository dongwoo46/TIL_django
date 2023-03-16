from django.shortcuts import render
# models에서 Article 임포트
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def create(request):
    return render(request, 'articles/create.html')

def getto(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    def __str__(self):
        return f'title : {self.title} / content : {self.content}'
    
    # 이 시점에 데이터 저장해보자!
    article = Article()
    article.title = title
    article.content = content
    article.save()
    print(title,content)
    context = {
        'article':article
    }

    return render(request, 'articles/getto.html',context)
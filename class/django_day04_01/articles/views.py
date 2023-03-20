from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    #데이터를 가져와서 템플릿에 저장
    articles  = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html',context)


def detail(request, pk):
    article = Article.objects.get(id=pk) # id는 pk로 바꿔도 ㄱㅊ
    context = {
        'article': article
    }

    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 사용자가 전송한 데이터 가져와서 DB에 저장
    title = request.POST.get('title') #title이란 name의 input값을 가져옴
    content = request.POST.get('content')
    
    #DB에 새로운 Article 바로 저장하는 방법
    # Article.objects.create(
    #     title=title,
    #     content=content,
    # )

    #DB에 새로운 Article 뭔가 로직 추가하고 저장하는 방법 이방법이 더 많이쓰임
    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:index')

#GET은 데이터를 가저 올때(조회)할 때만 사용한다!!!!!
#Post방식으로 데이터 전달하면 쿼리스트링이 아님! 데이터가 가려짐!
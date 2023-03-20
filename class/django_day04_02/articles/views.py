from django.shortcuts import render, redirect
#  2. Article모델 클래스 import!!
from .models import Article
# Create your views here.
def index(request):
    # 1. 전체 게시글 불러오기
    # 2. QureySet API all() 이용해서 전체 데이터 가져오기
    article_list = Article.objects.all()
    # 3. 가져온 데이터를 html 템플릿에 보여지도록 context로 전달하기
    context = {
        'article_list':article_list,

    }
    return render(request, 'articles/index.html', context)







# variable routing 에서 전달되는 정보를 반드시 인자로 받아야함(pk)

def detail(request, pk):
    # 1. 받은 pk값을 이용해서 DB에서 데이터 찾아옴. .get()
    article = Article.objects.get(id=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

# 사용자에게 입력 form을 보여주기 위한 함수
# def new(request):
#     return render(request, 'articles/new.html')

# 새 데이터 만들기
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # 첫 번째 저장 방법
        article = Article()
        article.title = title
        article.content = content
        article.save()

        # 글 상세페이지로 이동 (redirect는 다른 주소로 보낼때)
        # 여기선 파이썬이 적용되기 때문에 ,로 구분 html에서는 띄어쓰기로 구분
        return redirect('articles:detail', article.pk)      
    else:
        return render(request, 'articles/new.html')

def delete(request, pk):
    # 삭제하기 위해서는 DB에서 대상을 찾아와야함
    article = Article.objects.get(id=pk)
    
    # 2. delete() 이용해서 삭제하면 끝
    article.delete()
    # 3. index 
    return redirect('articles:index')

# create와 차이점 값을 보여줘야한다.
def edit(request,pk):
    # 수정할 데이터를 가져온다.
    article = Article.objects.get(id=pk)
    context = {
        'article': article,

    }
    return render(request, 'articles/edit.html', context)


#수정하기
def update(request, pk):
    # 1. 수정할 글을 불러온다.
    article = Article.objects.get(id=pk)

    # 2. 사용자가 수정한 내용을 적용한다. 
    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)

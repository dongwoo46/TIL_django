from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html') # 사용자에게 html 파일을 제공하고자 할때 사용
    
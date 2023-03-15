from django.shortcuts import render

# Create your views here.
def index(request):
    menus = ['사과','짜장면','김밥','라면','보쌈','치킨']
    users = []
    context = {
        'menus':menus,
        'users':users,
    }
    return render(request, 'articles/article.html',context)
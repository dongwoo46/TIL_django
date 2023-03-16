from django.shortcuts import render
from datetime import datetime

# Create your views here.
def article(request):
    menus = ['사과','짜장면','김밥','라면','보쌈','치킨']
    users = []
    today = datetime.now()
    context = {
        'menus':menus,
        'users':users,
        'today':today
    }
    return render(request, 'articles/article.html',context)